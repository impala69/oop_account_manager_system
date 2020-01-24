from Invoice import Invoice
from InvoiceFactory import InvoiceFactory

class Invoices:
    def __init__(self):
        self.invoices = []

    def delete_invoice(self, invoice_object):
        self.invoices.remove(invoice_object)
        return self.invoices

    def add_invoice(self, invoice_type, *args, **kwargs):
        invoice_object = Invoice.create_invoice(*args, **kwargs)
        invoice_type_object = InvoiceFactory.generate_invoice_object(invoice_type=invoice_type)
        invoice_type_object.create_invoice(invoice_object=invoice_object)
        self.invoices.append(invoice_type_object)
        return invoice_object

    def get_invoice(self, factor_number):
        for item in self.invoices:
            if item.invoice_object.factor_number == factor_number:
                return item
        return False

    def search_invoice(self,search_starategy_obj ,search_params):
        search_starategy_obj.searching(search_params)

    def list_invoices(self):
        return self.invoices

    def get_invoices_per_supplier(supplier):
        result_list = []
        for i in self.invoices:
            if i.supplier is supplier:
                result_list.append(i)
        return result_list



all_invoices = Invoices()
all_invoices.add_invoice("PURCHASE", 1, "CREDIT", 0, 0, 10000, 1)
