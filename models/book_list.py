from models.book import *
import datetime


# event1 = Event(datetime.date(2022, 12, 6), "Misha's birthday", 25, "Edinburgh", "birthday party", True)
book1 = Book("How to build a car", "Adrian Newey", "Autobiography, Biography", "floor 2, shelf 2", 1, "The world’s foremost designer in Formula One, Adrian Newey OBE is arguably one of Britain’s greatest engineers and this is his fascinating, powerful memoir. How to Build a Car explores the story of Adrian’s unrivalled 35-year career in Formula One through the prism of the cars he has designed, the drivers he has worked alongside and the races in which he’s been involved A true engineering genius, even in adolescence Adrian’s thoughts naturally emerged in shape and form – he began sketching his own car designs at the age of 12 and took a welding course in his school summer holidays. From his early career in IndyCar racing and on to his unparalleled success in Formula One, we learn in comprehensive, engaging and highly entertaining detail how a car actually works. Adrian has designed for the likes of Mario Andretti, Nigel Mansell, Alain Prost, Damon Hill, David Coulthard, Mika Hakkinen, Mark Webber and Sebastian Vettel, always with a shark-like purity of purpose: to make the car go faster. And while his career has been marked by unbelievable triumphs, there have also been deep tragedies; most notably Ayrton Senna’s death during his time at Williams in 1994. Beautifully illustrated with never-before-seen drawings, How to Build a Car encapsulates, through Adrian’s remarkable life story, precisely what makes Formula One so thrilling – its potential for the total synchronicity of man and machine, the perfect combination of style, efficiency and speed.")
book2 = Book("The Golden Ratio", "Gary B Meisner", "Science, Art, Mathematics,Design", "floor 3, shelf 21", 5,"The Golden Ratio examines the presence of this divine number in art and architecture throughout history, as well as its ubiquity among plants, animals, and even the cosmos. This gorgeous book features clear, entertaining, and enlightening commentary alongside stunning full-color illustrations by Venezuelan artist and architect Rafael Araujo. From the pyramids of Giza, to quasicrystals, to the proportions of the human face, the golden ratio has an infinite capacity to generate shapes with exquisite properties. With its lush format and layflat dimensions that closely approximate the golden ratio, this is the ultimate coffee table book for math enthusiasts, architects, designers, and fans of sacred geometry.")
book3 = Book("Stolen Focus: Why You Can't Pay Attention", "Johann Hari", "Psychology, Self Help Science","floor 1, shelf 12", 10,"In the United States, teenagers can focus on one task for only sixty-five seconds at a time, and office workers average only three minutes. Like so many of us, Johann Hari was finding that constantly switching from device to device and tab to tab was a diminishing and depressing way to live. He tried all sorts of self-help solutions--even abandoning his phone for three months--but nothing seemed to work. So Hari went on an epic journey across the world to interview the leading experts on human attention--and he discovered that everything we think we know about this crisis is wrong. We think our inability to focus is a personal failure to exert enough willpower over our devices. The truth is even more disturbing: our focus has been stolen by powerful external forces that have left us uniquely vulnerable to corporations determined to raid our attention for profit. Hari found that there are twelve deep causes of this crisis, from the decline of mind-wandering to rising pollution, all of which have robbed some of our attention. In Stolen Focus, he introduces readers to Silicon Valley dissidents who learned to hack human attention, and veterinarians who diagnose dogs with ADHD. He explores a favela in Rio de Janeiro where everyone lost their attention in a particularly surreal way, and an office in New Zealand that discovered a remarkable technique to restore workers' productivity. Crucially, Hari learned how we can reclaim our focus--as individuals, and as a society--if we are determined to fight for it. Stolen Focus will transform the debate about attention and finally show us how to get it back.")
books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)


def delete_book(book_name):
    book_to_delete = None
    for book in books:
        if book.title == book_name:
            book_to_delete = book
            break

    books.remove(book_to_delete)
    
