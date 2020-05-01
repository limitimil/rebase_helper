config = [
        {
                'repository_url':'http://tfs.cybersoft4u.com.tw:8080/tfs/SDD/TIS/_git/CloudTisTesting',
                'branches': [
                    'tool-CTIS-xxxx',
                    'tool-CTIS-2149',
                    ],
                'plugin_actions': {
                        'python-lint':{
                                'name': 'python-lint',
                                'targets': ['testtools', 'testutils', 'unittests'],
                        }
                }
        },
]
