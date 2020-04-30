import change_pythonpath
import dynatrace.topology.hosts as hosts
import dynatrace.tenant.management_zones as mz
import user_variables as uv

# YOUR SCRIPT GOES HERE

cluster = uv.FULL_SET['CLUSTER_NAME']
tenant = "TENANT_NAME"
mz_list = mz.get_management_zone_list(cluster, tenant)

for zone in mz_list:
  print ("Management Zone: " + zone['name'] + "\tHost Units: ", end="")
  print(hosts.get_host_units_tenantwide(cluster, tenant, params={"managementZone": zone['id']}))