groom = "Chris"
bride = "Annika"
congratulants = ["Judith", 
                 "Kamal", 
                 "Clemens", 
                 "Daniel", 
                 "Anna-Lena", 
                 "Simeon", 
                 "Joy", 
                 "Sebastian", 
                 "Selina", 
                 "Peter", 
                 "Léa", 
                 "Fabienne", 
                 "Jake", 
                 "Markus", 
                 "Steffi", 
                 "Elli", 
                 "Ellen", 
                 "Tina", 
                 "Alison", 
                 "Philipp", 
                 "Alexander", 
                 "Katharina", 
                 "Maximilian", 
                 "Carsten S.", 
                 "Christine", 
                 "Nico",
                 "Merlin🐶"]

def best_wishes(groom, bride, congratulant):
    message = (
    """
    Lieber {}, liebe {},
    zu eurer Hochzeit wünschen wir euch alles erdenklich Gute!
    Wir freuen uns mit euch und hoffen, ihr hattet einen wunderschönen Tag.
    Euer Myxo {}
    """.format(groom, bride, congratulant))
    
    return message

for congratulant in congratulants:
    print(best_wishes(groom, bride, congratulant))
