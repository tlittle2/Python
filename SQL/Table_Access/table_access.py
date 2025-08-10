class TableAccess:
    def __init__(self):
        pass

    class Process_Ranges_Table:
        def __init__(self):
            pass
          
        def get_process_ranges2(self, process_name: str, run_number: int)-> str:
            sql = "select lower_bound,upper_bound from process_ranges_parm where process_name = '{}' and run_number = {};".format(process_name, run_number)
            return sql


def main():
    o = TableAccess().Process_Ranges_Table()
    print(o.get_process_ranges2("PROCESS SALARIES", 1))

if __name__ == "__main__":
    main()
