# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 08:57:29 2019

@author: Patrick H. Patin
"""

# Make sure our file paths work for Mac & Windows
import os
import csv


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#=================================================================================
#                       METHOD DEFINITIONS SECTION START
#=================================================================================
#¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡


# --------------------------------------------------------------------------------
#  ProcessBudgetFile - compiles the information in the Budget File and outputs results
#       - Output results to console
#       - Output results to Budget_Analysis_PHP.txt
# --------------------------------------------------------------------------------
def ProcessBudgetFile(BudgetFile):
    dblLastValue = 0
    dblTotalRevenue = 0
    dblCurrentValue = 0
    dblProfitLoss = 0
    sCurrentDate = ""
    sLastDate = ""
    
    iTotalMonths = 0
    dblNetProfitLoss = 0    
    dblAverageChange = 0
    
    sGIDate = ""
    dblGIValue = 0
    sGDDate = ""
    dblGDValue = 0
    
    # Budget File First
    with open(BudgetFile, 'r') as csvFile:
        csvReader = csv.reader(csvFile)
        
        # Skip the header but store it in a variable because it's part of the assignment
        # even though we aren't using these values
        myHeader = next(csvReader)
        
        # Loop over the rest of the data
        for sLine in csvReader:
            # Increment our month counter and read our current values
            iTotalMonths += 1
            sCurrentDate = sLine[0]
            dblCurrentValue = float(sLine[1])
            
            # Is this the first record?
            if iTotalMonths == 1:
                dblTotalRevenue = dblCurrentValue
            elif len(sLastDate) >= 1 and iTotalMonths > 1:
                dblProfitLoss = dblCurrentValue - dblLastValue
                dblNetProfitLoss = dblNetProfitLoss + dblProfitLoss
                dblTotalRevenue = dblTotalRevenue + dblCurrentValue
                
                # Is this the greatest value we've seen yet?
                if dblGIValue < dblCurrentValue - dblLastValue:
                    sGIDate = sCurrentDate
                    dblGIValue = round(dblCurrentValue - dblLastValue, 2)
                # Or, is this the lowest value we've seen yet
                elif dblGDValue > dblCurrentValue - dblLastValue:
                    sGDDate = sCurrentDate
                    dblGDValue = round(dblCurrentValue - dblLastValue, 2)
            
            # Set the lastDate and LastValue to the Current Value for the next loop
            sLastDate = sCurrentDate
            dblLastValue = dblCurrentValue
        # next sLine
    # end with
    
    # Format values
    dblAverageChange = dblNetProfitLoss / (iTotalMonths - 1)
    dblNetProfitLoss = '{:0,.2f}'.format(dblNetProfitLoss)
    dblAverageChange = '{:0,.2f}'.format(dblAverageChange)
    dblTotalRevenue = '{:0,.2f}'.format(dblTotalRevenue)
    dblGIValue = '{:0,.2f}'.format(dblGIValue)
    dblGDValue = '{:0,.2f}'.format(dblGDValue)
    
    # Done looping through the file
    # Print out results to the console
    print("-------------------------------------")
    print("Financial Analysis of the Budget File")
    print("-------------------------------------")
    print(f"Total Months: {iTotalMonths}")
    print(f"Total: $ {dblTotalRevenue}")
    print(f"Average Change: $ {dblAverageChange}")
    print(f"Greatest Increase in Profits: {sGIDate} ($ {dblGIValue})")
    print(f"Greatest Decrease in Profits: {sGDDate} ($ {dblGDValue})")
    print("-------------------------------------")
    
    # Print out the results to a text file
    with open("Budget_Analysis_PHP.txt", "w") as myOutputFile:
        myOutputFile.write("-------------------------------------\n")
        myOutputFile.write("Financial Analysis of the Budget File\n")
        myOutputFile.write("-------------------------------------\n")
        myOutputFile.write(f"Total Months: {iTotalMonths}\n")
        myOutputFile.write(f"Total: $ {dblTotalRevenue}\n")
        myOutputFile.write(f"Average Change: $ {dblAverageChange}\n")
        myOutputFile.write(f"Greatest Increase in Profits: {sGIDate} ($ {dblGIValue})\n")
        myOutputFile.write(f"Greatest Decrease in Profits: {sGDDate} ($ {dblGDValue})\n")
        myOutputFile.write("-------------------------------------\n")
        myOutputFile.close
    # end with
# end ProcessBudgetFile()
        

# --------------------------------------------------------------------------------
#  TallyVotes - compiles the information in the Poll Data File and outputs results
#       - Output results to console
#       - Output results to Election_Results_PHP.txt
# --------------------------------------------------------------------------------
def TallyVotes(VoteFile):
    # Budget File First
    with open(VoteFile, 'r') as csvFile:
        csvReader = csv.reader(csvFile)
        
        # Skip the header but store it in a variable because it's part of the assignment
        # even though we aren't using these values
        myHeader = next(csvReader)
        bFirstDataRow = True
        
        # Number of records.  Keep in mind:
        #   - We aren't counting the header row
        #   - We are treating the first data row differently
        #   - So, start with one and only incriment after the first data row
        RecCounter = 1
        
        # Loop over the rest of the data
        for sLine in csvReader:
            # Is this the first record?
            if bFirstDataRow == True:
                bFirstDataRow = False
                Candidates = [sLine[2]]
                Votes = [1]
                WasFound = True
            else:
                # Our data record counter
                RecCounter += 1
                # Hasn't been found yet
                WasFound = False
                # Reset to zero on each parent loop
                CandidateCounter = 0
                
                for eachCandidate in Candidates:
                    if eachCandidate == sLine[2]:
                        Votes[CandidateCounter] += 1
                        WasFound = True
                        break
                    # end if
                    
                    CandidateCounter += 1
                # next
            # end if
            
            if WasFound == False:
                Candidates.append(sLine[2])
                Votes.append(1)
            # end if
        # next sLine
    # end with
    
    # Print out the results to a text file
    with open("Voting_Results_PHP.txt", "w") as myOutputFile:
        # Done looping through the file
        # Print out results to the console and to our output file
        print("-------------------------------------")
        print("The Official Election Results")
        print("-------------------------------------")
        print(f"Total Votes: {'{:0,}'.format(RecCounter)}")
        print("-------------------------------------")
        
        myOutputFile.write("-------------------------------------\n")
        myOutputFile.write("The Official Election Results\n")
        myOutputFile.write("-------------------------------------\n")
        myOutputFile.write(f"Total Votes: {'{:0,}'.format(RecCounter)}\n")
        myOutputFile.write("-------------------------------------\n")
        
        # reset the counter
        Counter = 0
        MostVotes = 0
        
        for eachRec in Candidates:
            if Votes[Counter] > MostVotes:
                MostVotes = Votes[Counter]
                sWinner = eachRec
            # end if
            
            # Calculate the Candidates Vote Percentage
            dblPercent = Votes[Counter] / RecCounter * 100
            
            # Print & Write each candidates Voting Tallies
            print(f"{Candidates[Counter]}: {'{:0,.3f}'.format(dblPercent)}% ({'{:0,}'.format(Votes[Counter])})")
            myOutputFile.write(f"{Candidates[Counter]}: {'{:0,.3f}'.format(dblPercent)}% ({'{:0,}'.format(Votes[Counter])})\n")
            
            Counter += 1
        # next
        
        print("-------------------------------------")
        print(f"WINNER: {sWinner}")
        print("-------------------------------------")
        
        myOutputFile.write("-------------------------------------\n")
        myOutputFile.write(f"WINNER: {sWinner}\n")
        myOutputFile.write("-------------------------------------\n")
        myOutputFile.close
    # end with
# end TallyVotes()

#=================================================================================
#                       METHOD DEFINITIONS SECTION END
#=================================================================================
    
    
    
    
    


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#=================================================================================
#                         PYTHON SCRIPT SECTION START
#=================================================================================
#¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡
# Resource file locations
sBudgetFile = os.path.join("PyBank", "Resources", "budget_data.csv")
sVotingFile = os.path.join("PyPoll", "Resources", "election_data.csv")

# Does our Budget Resource File exist?
exists = os.path.isfile(sBudgetFile)
if exists == False:
    print("The Budget resource file could not be found.")
    print("")
    print("The following sub directories and files must exist in the location where this script runs (i.e.):")
    print("     " + os.path.join("...", "PyBank", "Resources", "budget_data.csv"))
else:
    ProcessBudgetFile(sBudgetFile)
# end if

# Put some space between the two console output sections
print("")
print("")

# Does our Voting Resource File exist?
exists = os.path.isfile(sVotingFile)
if exists == False:
    print("The Voting resource file could not be found.")
    print("")
    print("The following sub directories and files must exist in the location where this script runs (i.e.):")
    print("     " + os.path.join("...", "PyPoll", "Resources", "election_data.csv"))
else:
    TallyVotes(sVotingFile)
# end if

# Put some space between the last data section and our termination confirmation
print("")
print("")

# Tell the user we're done
print("Processing is complete.")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#=================================================================================
#                         PYTHON SCRIPT SECTION END
#=================================================================================
#¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡
