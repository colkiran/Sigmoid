class CompanyHead:

    companyhead = ""
    @classmethod
    def set_company_head(cls, chead):
        cls.companyhead = chead

    @classmethod
    def get_company_head(cls):
        return cls.companyhead


CompanyHead.set_company_head("Arjit")    
print(CompanyHead.get_company_head())