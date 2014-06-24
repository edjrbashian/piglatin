#!/usr/bin/python

import os, sys, re
import logging
from datetime import datetime
from dateutil import tz
from sql_db2 import *
import xlwt
from xlrd import open_workbook
from operator import itemgetter

class test_sql( sql_db_C):
  """
  @brief SQL database server access API

  """

  """
  Server: ssvweb (137.78.178.64)
  Database: iprw_desdyni
  User: report_builder
  Password: reports
  database: iprw_desdyni
  Privileges: Select on product, releasecollection, releasecollectionitem
  """

  hostname = 'ssvweb'
  username = 'report_builder'
  password = 'reports'
  database = 'iprw_desdyni'

  sql_fields = {



"""
+-------------------------+--------------+------+-----+------------+----------------+
| Field                   | Type         | Null | Key | Default    | Extra          |
+-------------------------+--------------+------+-----+------------+----------------+
| g_id                    | int(11)      | NO   | PRI | NULL       | auto_increment | 
| owner                   | varchar(255) | NO   |     | NULL       |                | 
| name                    | varchar(255) | NO   |     | NULL       |                | 
| caption                 | text         | NO   |     | NULL       |                | 
| caption_status          | varchar(255) | NO   |     | NULL       |                | 
| sol                     | int(11)      | NO   |     | NULL       |                | 
| uploadtime              | int(11)      | NO   |     | NULL       |                | 
| status                  | varchar(255) | NO   |     | NULL       |                | 
| mimetype                | varchar(255) | NO   |     | NULL       |                | 
| intendeduser            | varchar(255) | NO   |     | NULL       |                | 
| revision                | int(11)      | NO   |     | 0          |                | 
| revisionof              | int(11)      | NO   |     | 0          |                | 
| childof                 | int(11)      | NO   |     | 0          |                | 
| locked                  | smallint(6)  | NO   |     | 0          |                | 
| attention               | tinyint(4)   | NO   |     | 0          |                | 
| hide                    | tinyint(4)   | NO   |     | 0          |                | 
| donotrelease            | tinyint(4)   | NO   |     | 0          |                | 
| tvonly                  | tinyint(4)   | NO   |     | 0          |                | 
| product_approval_status | varchar(255) | NO   |     | Unapproved |                | 
| released                | smallint(6)  | NO   |     | 0          |                | 
| deleted                 | smallint(6)  | NO   |     | 0          |                | 
| pia_number              | varchar(20)  | NO   |     | NULL       |                | 
+-------------------------+--------------+------+-----+------------+----------------+
"""
    'product':                 # Fields for aquarius
    { 'source': 'VARCHAR( 300 ) NULL DEFAULT NULL',
      'rgb_1440x720' : 'VARCHAR( 300 ) NULL DEFAULT NULL',
      'values_1440x720' : 'VARCHAR( 300 ) NULL DEFAULT NULL',
      'eoe_values_2048x1024': 'VARCHAR( 300 ) NULL DEFAULT NULL',
      'eoe_rgb_2048x1024': 'VARCHAR( 300 ) NULL DEFAULT NULL',
      'eoe_cube_512x512': 'VARCHAR( 300 ) NULL DEFAULT NULL',
      'ipad_1440x720' : 'VARCHAR( 300 ) NULL DEFAULT NULL',
      'iphone_1024x512' : 'VARCHAR( 300 ) NULL DEFAULT NULL',
      'dds_4096x2048' : 'VARCHAR( 300 ) NULL DEFAULT NULL',      
      'dds_2048x1024' : 'VARCHAR( 300 ) NULL DEFAULT NULL',      
      'rgb_for_dds_2048x1024' : 'VARCHAR( 300 ) NULL DEFAULT NULL',      
      'rgb_for_dds_4096x2048' : 'VARCHAR( 300 ) NULL DEFAULT NULL',      
      'data_days' : 'VARCHAR( 300 ) NULL DEFAULT NULL',      
      },


    }

  def __init__ (self):
    """
    @brief initialize
    
    """
    self._sql = sql_db_C()

  def connect(self):
    """
    @brief make a connection

    @return True if successful, False if not
    """
    try:
      print 'connecting'
      self._sql.connect( test_sql.hostname,
                         test_sql.username,
                         test_sql.password,
                         test_sql.database)
      self._Cursor = self._sql._Cursor
      
      return True

    except:
      logging.error( 'Failed to connect to sql server')
      return False


    


if __name__ == '__main__':

  print 'Main'

  sql_server = test_sql()
  sql_server.connect()          # Connect

  table = 'product'



  field = 'g_id'
  #sql_string = 'select %s from %s' % ( field, table)
  sql_string='SELECT product.g_id, product.name, title  FROM product, releasecollectionitem, releasecollection WHERE product.g_id=releasecollectionitem.g_id AND releasecollectionitem.rcid=releasecollection.rcid;'
  sql_server.execute( sql_string)
  id_list = sql_server.fetchall()
  print id_list
  id_list_no_space = []
  for each in id_list:
  	id_list_no_space.append(( each[0], # id_number
                              re.sub("^\s+", "", each[1]), # name_string
                              re.sub("^\s+", "", each[2])  # title_string
                              )
                            )
                       	
  id_list = sorted(id_list_no_space, key=itemgetter(2,)) #using operator module, list is sorted in relation to #2 column
  
  style = xlwt.XFStyle() # Create the Style 
  font = xlwt.Font() # Create the Font  
  font.height = 220  
  style.font = font # Apply the Font to the Style
  
  style1 = xlwt.XFStyle() # Create the Style 
  font = xlwt.Font() # Create the Font  
  font.height = 220
  font.bold = True 
  style1.font = font # Apply the Font to the Style
  
  style2 = xlwt.XFStyle() # Create the Style 
  font = xlwt.Font() # Create the Font  
  font.height = 220
  font.colour_index = 4
  style2.font = font # Apply the Font to the Style
  
  style3 = xlwt.XFStyle() # Create the Style 
  font = xlwt.Font() # Create the Font  
  font.height = 220
  font.bold = True
  #font.colour_index = 11
  style3.font = font # Apply the Font to the Style

  	
  workbook = xlwt.Workbook(encoding = 'ascii')
  worksheet = workbook.add_sheet('id_name')

  for row, id in enumerate(id_list):
    id_number = id[0]           # Pick the first
    name_string = id[1]
    title_string= id[2]
    
   

    worksheet.write( row+2, 0, id_number, style1) # Column 0 is id
    worksheet.write( row+2, 1, name_string, style) # Column 1 is name
    worksheet.write( row+2, 2, title_string, style3) #Column 2 is title
    worksheet.write( row+2, 3, xlwt.Formula('HYPERLINK("%s%s%s")' % ("http://transfer.jpl.nasa.gov/ssv/base/viewProduct.php?id=", id_number, "&iprw_database=iprw_desdyni")), style2)
    
    print 'row %d, %d, %s ' % (row, id_number,title_string)
    
    
style = xlwt.XFStyle() # Create the Style 
font = xlwt.Font() # Create the Font 
font.bold = True
font.colour_index = 2
font.height = 400  
style.font = font # Apply the Font to the Style



worksheet.write(0, 0, 'SSV#',style) #applying headers with style
worksheet.write(0, 1, 'Description',style)
worksheet.write(0, 2, 'Collection',style)
worksheet.write(0, 3, 'Weblink',style)


worksheet.col(1).width = 21600 #Set width to 6.5 inches
worksheet.col(2).width = 9999 #Set width to 3 inches
worksheet.col(3).width = 20000 #Set width to 6 inches



workbook.save( 'desdyni_final.xls')
print 'Done!'

