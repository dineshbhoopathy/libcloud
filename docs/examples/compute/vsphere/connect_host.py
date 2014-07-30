from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

cls = get_driver(Provider.VSPHERE)
driver = cls(host='192.168.1.100',
             username='admin', password='admin')
print(driver.list_nodes())
# ...