'''
Problem: Write a function that takes the number of computers in a cyber cafe (N) and a sequence of letters
         where the first occurence of a letter indicates a customer arriving, and the second the same customer leaving
         A customer leaves if no computer is available at the moment. Return the number of such customers.

Runtime: O(M) - M = length of sequence

URL: http://www.geeksforgeeks.org/function-to-find-number-of-customers-who-could-not-get-a-computer/
'''

def runComputerSimulation (N, seq):

    computersInUse = 0
    returnedCustomers = []
    customersInCafe = []

    for s in seq:

        # Customer already in cafe and the occurrence is second.
        # Hence, the customer is leaving
        ### in operator is O(n) i.e. O(N) in this case
        if s in customersInCafe:
            computersInUse-=1
            customersInCafe.remove(s)   ### O(N) time

        # Customer not in cafe.
        # New customer came in.
        # 2 possibilities: computersInUse == N -> Customer returned w/o use
        #               Or use increase computersInUse and add customer in cafe
        else:

            if computersInUse == N:
                if s not in returnedCustomers:      ### O(k) k=length of returned customers
                    returnedCustomers.append(s)     ### O(1)

            elif computersInUse < N:
                computersInUse+=1
                customersInCafe.append(s)

            else:
                raise Exception("Invalid situation. Computers in use greater than maximum computers")

    return returnedCustomers
                

N = int(raw_input("N = "))
sequence = raw_input("Sequence = ").strip().split(" ")

returnedCustomers = runComputerSimulation(N, sequence)

print "Customers returned without using a computer: ", returnedCustomers
print "Number of customers returned without using a computer: ", len(returnedCustomers)
