import rubrik_mosaic
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

''' Following run from shell:
export rubrik_mosaic_username=admin
export rubrik_mosaic_password=MyPass123
export rubrik_mosaic_node_ip=mosaic.demo.com
'''

mosaic = rubrik_mosaic.Connect()
mosaic.get_store_stats()
''' Example return
[
    {
        u'NFS_STORE': {
            u'store_url': u'file://localhost/mnt/datosio_verstore/',
            u'store_stats': {
                u'store_size': u'9.2 GB'
            },
            u'store_type': u'vfs_store',
            u'created_epoch': 1554157793
        }
    }
]
'''