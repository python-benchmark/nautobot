# Generated by Django 3.2.18 on 2023-03-22 16:10

import sys

from django.db import migrations, models

import nautobot.ipam.utils.migrations


def reverse_it(apps, schema_editor):
    """Reverse Namespace migrations."""
    Namespace = apps.get_model("ipam", "Namespace")
    VRF = apps.get_model("ipam", "VRF")
    VRFDeviceAssignment = apps.get_model("ipam", "VRFDeviceAssignment")
    IPAddress = apps.get_model("ipam", "IPAddress")
    Prefix = apps.get_model("ipam", "Prefix")
    Interface = apps.get_model("dcim", "Interface")
    VMInterface = apps.get_model("virtualization", "VMInterface")

    ns_global = Namespace.objects.get(name="Global")
    Prefix.objects.update(namespace=ns_global)
    VRF.objects.update(namespace=ns_global)
    Namespace.objects.exclude(name=ns_global.name).delete()

    # Reset VRF-to-device/VM assignments.
    VRFDeviceAssignment.objects.all().delete()

    # Clear vrf from [VM]Interface objects.
    Interface.objects.update(vrf=None)
    VMInterface.objects.update(vrf=None)

    # Clear parenting.
    IPAddress.objects.update(parent=None, ip_version=None)
    Prefix.objects.update(parent=None, ip_version=None)

    # Remove objects created by migrations.
    Prefix.objects.filter(description__startswith="Created by Nautobot").delete()
    for vrf in VRF.objects.filter(description__startswith="Created by Nautobot"):
        original_vrf = (
            VRF.objects.exclude(description__startswith="Created by Nautobot")
            .filter(name=vrf.name, rd=vrf.rd, tenant=vrf.tenant)
            .first()
        )
        Prefix.objects.filter(vrf=vrf).update(vrf=original_vrf)
        vrf.delete()


def migrate_ipaddress_status_to_type(apps, schema_editor):
    """Migrate IPAddress.status DHCP/SLAAC to types."""
    Status = apps.get_model("extras", "Status")
    IPAddress = apps.get_model("ipam", "IPAddress")
    ContentType = apps.get_model("contenttypes", "ContentType")

    ips_dhcp = IPAddress.objects.filter(status__name="DHCP")
    ips_slaac = IPAddress.objects.filter(status__name="SLAAC")
    ipaddress_ct = ContentType.objects.get_for_model(IPAddress)

    # First, update update type on any IPs with status DHCP/SLAAC.
    if any([ips_dhcp.exists(), ips_slaac.exists()]):
        status_migrated, _ = Status.objects.get_or_create(
            name="Migrated",
            defaults={
                "color": "ff0000",
                "description": "DHCP/SLAAC status replaced with `type` of same name by Nautobot 2.0 data migrations.",
            },
        )
        status_migrated.content_types.add(ipaddress_ct)

        # Update all objects of status=DHCP to type=DHCP & status=Migrated.
        if "test" not in sys.argv:
            print(">>> Migrating IPAddresses with status DHCP to type DHCP...")

        ips_dhcp.update(type="dhcp", status=status_migrated)

        # Update all objects of status=SLAAC to type=SLAAC & status=Migrated.
        if "test" not in sys.argv:
            print(">>> Migrating IPAddresses with status SLAAC to type SLAAC...")

        ips_slaac.update(type="slaac", status=status_migrated)

    # Then, delete the legacy status objects.
    for status_name in ("DHCP", "SLAAC"):
        try:
            status = Status.objects.get(name=status_name)
            # Clear the IPAddress content-type no matter what.
            status.content_types.remove(ipaddress_ct)
            if not status.content_types.exists():
                print(f">>> Deleting Status {status_name}")
                status.delete()
        except (models.ProtectedError, Status.DoesNotExist):
            pass


def revert_ipaddress_type_to_status(apps, schema_editor):
    """Revert IPAddress.type DHCP/SLAAC to status."""
    Status = apps.get_model("extras", "Status")
    IPAddress = apps.get_model("ipam", "IPAddress")
    ContentType = apps.get_model("contenttypes", "ContentType")

    ipaddress_ct = ContentType.objects.get_for_model(IPAddress)
    defaults = {"color": "4caf50"}
    type_map = {
        "DHCP": "Dynamically assigned IPv4/IPv6 address",
        "SLAAC": "Dynamically assigned IPv6 address",
    }

    # Recreate the DHCP/SLAAC statuses.
    for type_name, description in type_map.items():
        ips = IPAddress.objects.filter(type=type_name.lower())
        if ips.exists():
            defaults["description"] = description
            status, _ = Status.objects.get_or_create(name=type_name, defaults=defaults)
            status.content_types.add(ipaddress_ct)
            ips.update(status=status)


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("dcim", "0045_ipam__namespaces"),
        ("extras", "0001_initial_part_1"),
        ("ipam", "0030_ipam__namespaces"),
        ("virtualization", "0023_ipam__namespaces"),
    ]

    operations = [
        migrations.RunPython(
            code=nautobot.ipam.utils.migrations.process_namespaces,
            reverse_code=reverse_it,
        ),
        migrations.RunPython(
            code=migrate_ipaddress_status_to_type,
            reverse_code=revert_ipaddress_type_to_status,
        ),
    ]