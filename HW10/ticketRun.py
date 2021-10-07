from ticket import Ticket
from textTicket import TextInterface

inter = TextInterface()
app = Ticket(inter)
app.start()
