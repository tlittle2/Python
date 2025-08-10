class SqlBuilder:
    p_select = []
    p_from = []
    p_where = []
    p_groupby= []
    p_orderby = []

    p_and = " and "
    p_or = " or "
    p_in = " in "
    p_select_all = "*"

    comma = ","
    space = " "

    def __init__(self):
        self.p_select = []
        self.p_from = []
        self.p_where = []
        self.p_groupby = []
        self.p_orderby = []

    def addParentheses(self, s: str):
        return f"({s})"

    def add(self, collection: list, s: str):
        collection.append(s)

    def get(self, collection: list, sep: str):
        return sep.join(collection)
        
    def setSelect(self, s: str):
        self.add(self.p_select, s)

    def setSelect2(self, c: list):
        for i in c:
            self.setSelect(i)
    
    def getSelect(self, sep: str = comma):
        return "select {}".format(self.get(self.p_select, sep))
    
    def setFrom(self, s: str):
        self.add(self.p_from, s)

    def setFrom2(self, c: list):
        for i in c:
            self.setFrom(i)

    def getFrom(self):
        return "from {}".format(self.get(self.p_from, self.comma))
    
    def setWhere(self, s: str, sep: str = space):
        assert(sep in [self.p_and, self.p_or, self.p_in, self.space])
        self.add(self.p_where, self.addParentheses(s) + " " + sep)

    def setWhere2(self, c: list, sep: str = space):
        assert(sep in [self.p_and, self.p_or, self.p_in, self.space])
        for i in c:
            self.setWhere(self.addParentheses(i), sep)

    def getWhere(self):
        return "where {} ".format(self.get(self.p_where, self.space))
    
    def setGroupBy(self, s: str):
        self.add(self.p_groupby, s)

    def setGroupBy2(self, c: list):
        for i in c:
            self.setGroupBy(i)
    
    def getGroupBy(self):
        return "group by {} ".format(self.get(self.p_groupby, self.comma)) 

    def setOrderBy(self, s: str):
        self.add(self.p_orderby, s)

    def setOrderBy2(self, c: list):
        for i in c:
            self.setOrderBy(i)

    def getOrderBy(self):
        return "order by {} ".format(self.get(self.p_orderby, self.comma))
    
    def getSql(self, includeWhere: bool = False, includeGroupBy: bool = False, includeOrderBy: bool = False):
        assert(len(self.p_select) > 0 and len(self.p_from) > 0)
        def eval(clause: list, b: bool):
            if(len(clause) > 0 and b):
                return True
            return False
        
        blank = ""

        return "{} {} {} {} {}".format(self.getSelect()
                              , self.getFrom()
                              , self.getWhere() if eval(self.p_where, includeWhere) else blank
                              , self.getGroupBy() if eval(self.p_groupby, includeGroupBy) else blank
                              , self.getOrderBy() if eval(self.p_orderby, includeOrderBy) else blank
                              )
