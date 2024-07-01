{
  'name': 'Chat Application',
  'version': '1.0.0',
  'category': 'Uncategorized',
  'author': 'Jay',
  'website': 'https://yourwebsite.com',  # Optional: Your website URL
  'license': 'LGPL-3',  # You can choose other licenses like GPL-2 or AGPL-3
  'summary': 'A short description of your module',
  'description': """
  A longer description of your module and its functionalities.
  """,
  'data': [
      'views/chat_view.xml',
      'views/attachment.xml',
      # 'security/student_security.xml',
      # 'security/ir.model.access.csv'
      
  ],
  'depends': [
    'base',
    'mail',
  ],
  'installable': True,  # Set to False if the module shouldn't be installable through the Odoo interface
  'application': True,  # Set to False if the module shouldn't be included in the main Odoo menu
  'auto_install': False,  # Set to True for automatic installation at Odoo startup (use with caution)
  'icon': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1VRQPj-FQDMn14jyqgO0sb9DGlCgQfEvN8A&s',  # Path to your module's icon image (optional)
}