class SqlBuilder:
    p_select = []
    p_from = []
    p_where = []
    p_groupby= []
    p_orderby = []
    p_join = []

    inner_join = "inner join"
    left_outer_join = "left outer join"
    right_outer_join = "right outer join"
    full_outer_join = "full outer join"

    p_and = "and"
    p_or = "or"
    p_in = "in"

    select_all = "*"
    comma = ","
    space = " "

    def __init__(self):
        self.p_select = []
        self.p_from = []
        self.p_where = []
        self.p_groupby = []
        self.p_orderby = []
        self.p_join = []

    def addParentheses(self, s: str) -> str:
        return f"({s})"

    def add(self, collection: list, s: str):
        collection.append(s)

    def get(self, collection: list, sep: str) -> str:
        return sep.join(collection)
        
    def setSelect(self, s: str):
        self.add(self.p_select, s)

    def setSelect2(self, c: list):
        for i in c:
            self.setSelect(i)
    
    def getSelect(self, sep: str = comma) -> str:
        return "select {}".format(self.get(self.p_select, sep))
    
    def setFrom(self, s: str):
        self.add(self.p_from, s)

    def setFrom2(self, c: list):
        for i in c:
            self.setFrom(i)

    def getFrom(self) -> str:
        return "from {}".format(self.get(self.p_from, self.comma))
    
    def setWhere(self, s: str, sep: str = space):
        assert(sep in [self.p_and, self.p_or, self.p_in, self.space])
        self.add(self.p_where, self.addParentheses(s) + self.space + sep)

    def setWhere2(self, c: list, sep: str = space):
        assert(sep in [self.p_and, self.p_or, self.p_in, self.space])
        for i in c:
            self.setWhere(self.addParentheses(i), sep)

    def getWhere(self) -> str:
        return "where {} ".format(self.get(self.p_where, self.space))
    
    def setGroupBy(self, s: str):
        self.add(self.p_groupby, s)

    def setGroupBy2(self, c: list):
        for i in c:
            self.setGroupBy(i)
    
    def getGroupBy(self)-> str:
        return "group by {} ".format(self.get(self.p_groupby, self.comma)) 

    def setOrderBy(self, s: str):
        self.add(self.p_orderby, s)

    def setOrderBy2(self, c: list):
        for i in c:
            self.setOrderBy(i)

    def getOrderBy(self) -> str:
        return "order by {} ".format(self.get(self.p_orderby, self.comma))
    
    def setJoin(self, table: str, on: str, joinType: str):
        assert(joinType in [self.inner_join, self.left_outer_join, self.right_outer_join, self.full_outer_join])
        self.p_join.append([joinType, table, on])

    def setJoin2(self, clause: list):
        assert(len(clause) == 3)
        self.setJoin(clause[0],clause[1],clause[2])
    
    def getJoin(self) -> str:
        s = ""
        for l in self.p_join:
            s += "{} {} on {} ".format(l[0], l[1], l[2])
        return s

    
    def getSql(self, includeWhere: bool = False, includeGroupBy: bool = False, includeOrderBy: bool = False, includeJoin: bool = False) -> str:
        assert(len(self.p_select) > 0 and len(self.p_from) > 0)
        def eval(clause: list, b: bool):
            if(len(clause) > 0 and b):
                return True
            return False
        
        blank = ""

        return "{} {} {} {} {}".format(self.getSelect()
                              , self.getFrom()
                              , self.getJoin() if eval(self.p_join, includeJoin) else blank
                              , self.getWhere() if eval(self.p_where, includeWhere) else blank
                              , self.getGroupBy() if eval(self.p_groupby, includeGroupBy) else blank
                              , self.getOrderBy() if eval(self.p_orderby, includeOrderBy) else blank
                              )

def main():
    sql = SqlBuilder()
    sql.setSelect2(["a.case_num" , "a.id" , "a.rank"])
    sql.setFrom2(["salary_data a"])
    sql.setWhere("a.case_num <= 100", sql.p_and)
    sql.setWhere("a.id <= 100")

    sql.setJoin("salary_data b", "a.case_num = b.case_num", sql.inner_join)
    sql.setJoin2(["salary_data c", "a.case_num = c.case_num", sql.left_outer_join])

    print(sql.getSql(includeWhere= True))

if __name__ == "__main__":
    main()
