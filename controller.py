from Db import Database as Db
from flask import jsonify, request
import os
from dotenv import load_dotenv
import jwt
from uuid import uuid4

load_dotenv()



def return_true(): return True


class Controller:

    def __init__(self, table_name, modify_data=None, security_checker=return_true(), validate_data=return_true,allowed_gets=[],required_post_rows = []):
        self.table_name = table_name
        self.mod_data = modify_data
        self.security_check = security_checker

        self.dco = validate_data  # data consistency object
        self.alq = allowed_gets  # query criteria
        self.rpr = required_post_rows
        self.user = {}


    def post(self):
        check = self.security_check()
        if check != True: return check

        body = request.json
        if self.mod_data: self.mod_data(request.json)
        for key in self.rpr: #basic validate
            if not body[key]:
                return jsonify({"data": f"missing required row f{key}"})
        return jsonify({"data": f"{self.create_from_dict(body)} row(s) affected."})


    def put(self):
        check = self.security_check()
        if check != True: return check

        body = request.json
        for key in self.rpr: #basic validate
            if not body[key]:
                return jsonify({"data": f"missing a required row f{key}"})

        return jsonify({"data": f"{self.update_from_dict(body)} row(s) affected."})

    
    def get(self):
        check = self.security_check()
        if check != True: return check

        sql_where = "where status = 'ACTIVE' "
        for col in self.alq:
            arg = request.args.get(col["arg"])
            if arg: sql_where += f"and {col["name"]} {col["comparator"]} '{arg}'"
        data = {"data": Db.query(f"select * from {self.table_name} {sql_where};")}
        return jsonify(data)

    def delete(self):
        check = self.security_check()
        if check != True: return check


        item_id = request.args.get('id')
        if item_id:
            row_count = Db.query(f"""UPDATE {self.table_name} SET "status" = 'DELETED' WHERE "id" = '{item_id}'""")
            return jsonify({"data": f"{row_count} row(s) affected."})
        else:
            return jsonify({"data": "Please provide an id"})

    def create_from_dict(self, obj):
        obj["id"] = str(uuid4())
        col_names = ",".join(list(obj.keys()))
        col_values = ""
        for val in obj.values():
            val_type = type(val)

            if val_type is str:
                col_values += f"'{val}',"
            if val_type is int:
                col_values += f"{val},"
            if val_type is bool:
                col_values += "true," if val else "false,"
            if val_type is dict:
                col_values += f"'{str(val).replace("'", '"')}'::json,"
            if val_type is bytes:
                print(str(val))
                col_values += f"'{str(val)[2:-1]}',"
            if val is None:
                col_values += "NULL,"
        return Db.query(f"""insert into {self.table_name} ({col_names}) values ({col_values[:-1]});""")

    def update_from_dict(self, obj):
        template = """ "{col_name}" = {col_value},"""
        set_val = ""
        where_val = ""

        for k, v in obj.items():
            val = None
            val_type = type(v)

            if val_type is str:
                val = f"'{v}'"
            if val_type is int:
                val = f"{v}"
            if val_type is bool:
                val = "true," if v else "false"
            if val_type is dict:
                val = f"'{str(v).replace("'", '"')}'::json"
            if v is bytes:
                val = f"'{str(v)}'"
            if v is None:
                val = "NULL"
            if k == "id":
                where_val = template.format(col_name=k, col_value=val)
            else:
                set_val += template.format(col_name=k, col_value=val)

        sql = f"""UPDATE {self.table_name} SET {set_val[:-1]} WHERE {where_val[:-1]};"""
        return Db.query(sql)



    def isUserAllowed(self,account_id,user_id):
        try:
            print(Db.query(f"SELECT COUNT(*) > 0 as is_allowed  from acc_users au where au.acc_id ='{account_id}' and au.user_id ='{user_id}'"))
        except:
            return False

def handle_controller(controller):
    if request.method == 'GET':
        return controller.get()
    elif request.method == 'POST':
        return controller.post()
    elif request.method == 'PUT':
        return controller.put()
    elif request.method == 'DELETE':
        return controller.delete()

