import change_pythonpath
import dynatrace.topology.hosts as t_h
import dynatrace.cluster.users as users
import dynatrace.tenant.management_zones as management_zones
import user_variables
import json

def get_application_count(cluster, tenant):
  # This function takes every MZ it finds and counts everything 
  # before the first "-" as the app name. It will return the number of
  # "apps" it finds

  all_zones = management_zones.get_management_zone_list(cluster, tenant)
  application_list = []
  for zone in all_zones:
    zone_name = zone['name'].split(" - ")
    app_name = zone_name[0]
    if app_name not in application_list:
      application_list.append (app_name)
  return len(application_list) 

full_set = user_variables.FULL_SET  
cluster = user_variables.FULL_SET['selfmanaged']

print("Set Host Count: " + str(t_h.get_host_count_setwide(full_set)))
print("User Count: " + str(users.get_user_count(cluster)))



print("Customer Applications: " + str(get_application_count(cluster, 'sandbox')))
