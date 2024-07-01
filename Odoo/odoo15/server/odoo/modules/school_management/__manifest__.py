{
  'name': 'School Management',
  'version': '1.0.0',
  'category': 'Uncategorized',
  'author': 'Jay',
  'website': 'https://yourwebsite.com',  # Optional: Your website URL
  'license': 'LGPL-3',  # You can choose other licenses like GPL-2 or AGPL-3
  'summary': 'A short description of your module',
  'description': """
  A longer description of your module and its functionalities.
  """,
#   'depends': ['base'],  # List of module dependencies (replace 'base' with actual dependencies)
#   'data': [
#       'security/ir.model.access.csv',  # Security rules (optional)
#       'views/your_view.xml',  # Your module's views
#   ],
#   'demo': [
#       'demo/demo_data.xml',  # Optional: Demo data for your module
#   ],
  'installable': True,  # Set to False if the module shouldn't be installable through the Odoo interface
  # Optional fields
  'application': True,  # Set to False if the module shouldn't be included in the main Odoo menu
  'auto_install': False,  # Set to True for automatic installation at Odoo startup (use with caution)
  'icon': 'image.png',  # Path to your module's icon image (optional)
}