#!/bin/python

import os,sys
import re

regex = r"\bcast\s*\(\s*(\s*(\S+)\s*\/\s*1000\s+as\s+timestamp\)"
substitute = "udfs.timestampudf(\\1)"

viewddlsfile = sys.argv[1]
modified_ddl_file = sys.argv[2]
skipped_ddl_file = sys.argv[3]
select_stmts_file = sys.argv[4]

modified_ddl = open(modified_ddl_file,"w")
skipped_ddl = open(skipped_ddl_file,"w")
select_stmts = open(select_stmts_file,"w")

fileobj = open(viewddlsfile,'r')
lines = fileobj.readlines()

for line in lines:
  ddl_ended = False
  if '|' in line:
      line_list = line.split('|')
      dbname = line_list[0]
      view = line_list[1]
      ddl = line_list[2]
  else:
      if 'endofsql' in line:
          ddl_ended = True
      else:
          ddl += line.replace("\n"," ")
     
  if ddl_ended:
       is_matched = bool(re.search(regex,ddl, re.IGNORECASE | re.MULTILINE))
       if is_matched:
            result = re.sub(regex, substitute, ddl, 0, re.MULTILINE | re.IGNORECASE)
            if result:
                 drop_stmt = 'DROP VIEW ' + dbname.strip() + '.' + view.strip() + ';'
                 modified_ddl.write(drop_stmt)
                 modified_ddl.write("\n")
                 newddl = 'CREATE VIEW ' + dbname.strip() + '.' + view.strip() + ' AS ' + result + ';'
                 modified_ddl.write(newddl + "\n")
                 select_stmts.write(result.replace("\n"," ") + " limit 1;" + "\n" )
            else:
                 skipped_ddl.write("CREATE VIEW " + dbname.strip() + "." + view.strip() + " AS " + ddl + ";" )
                 skipped_ddl.write("\n")
                  
 modified_ddl.close()
 skipped_ddl.close()
 select_stmts.close()
