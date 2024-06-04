import psycopg2

def createDict(keys, tup):
    di = {}
    for i in range(0,len(keys)):
        di[keys[i]] = tup[i]
    return di

class Db ():

    def query(self, query):
        print(query)
        conn = psycopg2.connect(
            database="davin", user='postgres', password='password', host='127.0.0.1', port= '5432'
        )
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
            try:
                colnames = [desc[0] for desc in cur.description]
                return  list(map(lambda x: createDict(colnames,x),cur.fetchall()))
            except TypeError:
                return cur.rowcount

    def Stream(self):
        pass
        # something like the chunks below, scale not big enough to bother
        # Response(event_stream(), content_type='text/event-stream')
        #chunk_size = 1000  # Adjust this value based on your memory constraints and requirements
        # while True:
        #     rows = cur.fetchmany(chunk_size)
        #     if not rows:
        #         break
        #     for row in rows:
        #         # Process each row
        #         print(row)


    def testConn(self):
        print(self.query("select version()"))


Database = Db()
