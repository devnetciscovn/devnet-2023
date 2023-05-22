def build_vrf_configuration(vrf_name, rd, rt_import='', rt_export=''):
    rt_import_value = rt_import if rt_import else rd
    rt_export_value = rt_export if rt_export else rd

    # a = b if condition else c

    return f"""
    vrf {vrf_name}
    rd {rd}
    address-family ipv4
    route-target import {rt_import_value}
    route-target export {rt_export_value}
    """