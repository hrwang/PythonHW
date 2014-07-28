
1. for 1d dict, we could initiate it by "dict={}", and use directly with
variable, dict[variable]=values
0. Using a tuple as key to avoid 2d dictionary.
1. Make sure iterating a list of dictionary. The thing is a dictionary. See
problem 3-2.
2. If assigning a value to a 2d dict, using the defaultdict from collections.
See problem 3-2.
3. access dictionary: <code>dict['keyLevel1']['keylevel2']</code>
6. Solution 6-4: Does dict change the order of its items? Possible bug.



    import csv 
    import os
    import time
    
    def read_csv(path):
        """ 
        Reads the CSV file at path, and returns a list of rows. Each row is a
        dictionary that maps a column name to a value in that column, as a string.
        """
        output = []
        for row in csv.DictReader(open(path)):
            output.append(row)
        return output



    #read_csv( "./data/2008-results.csv")


    ################################################################################
    # Problem 1: State edges
    ################################################################################
    
    def row_to_edge(row):
        """ 
        Given an election result row or poll data row, returns the Democratic edge
        in that state.
        """
        return float(row["Dem"]) - float(row["Rep"])  
    
    def state_edges(election_result_rows):
        edges={}
        for row in election_result_rows:
            country=row['State']
            edge=row_to_edge(row)
            edges[country]=edge
        return edges
        """
        Given a list of election result rows, returns state edges.
        The input list does has no duplicate states;
        that is, each state is represented at most once in the input list.
        """



    ### Test for problem 1
    """
    rows2 = [{'State': 'WA', 'Dem': '1.0', 'Rep': '0.1'}]#,
            #{'State': 'CA', 'Dem': '0.2', 'Rep': '1.3'}
    
    
    #assert state_edges(rows2) == {'WA': 0.9, 'CA': -1.1}
    
    state_edges(rows2)
    #print rows2
    
    """




    "\nrows2 = [{'State': 'WA', 'Dem': '1.0', 'Rep': '0.1'}]#,\n        #{'State': 'CA', 'Dem': '0.2', 'Rep': '1.3'}\n\n\n#assert state_edges(rows2) == {'WA': 0.9, 'CA': -1.1}\n\nstate_edges(rows2)\n#print rows2\n\n"




    ### Solution for Problem 2
    
    import time
    def earlier_date(date1, date2):
        """
        Given two dates as strings (formatted like "Oct 06 2012"), returns True if 
        date1 is after date2.
        """
        return (time.strptime(date1, "%b %d %Y") < time.strptime(date2, "%b %d %Y"))
    
    def most_recent_poll_row(poll_rows, pollster, state):
        """
        Given a list of poll data rows, returns the most recent row with the
        specified pollster and state. If no such row exists, returns None.
        """
        recent={}
        for row in poll_rows:
            pster=row['Pollster']
            stat=row['State']
            dt=row['Date']
            if (pster,stat) in recent:
                if earlier_date (recent[(pster,stat)]['Date'],dt):
                    recent[(pster,stat)]=row                         ###using a tuple as key, avoiding 2d dictionary.
            else: 
                recent[(pster,stat)]=row
        if (pollster,state) in recent:
            return recent[(pollster,state)]
        else:
            return 'None'


    ###### Test problem 2
    """
    poll_rows1 = [{"ID":1, "State":"WA", "Pollster":"A", "Date":"Jan 07 2010"},
                  {"ID":2, "State":"WA", "Pollster":"B", "Date":"Mar 21 2010"},
                  {"ID":3, "State":"WA", "Pollster":"A", "Date":"Jan 08 2010"},
                  {"ID":4, "State":"OR", "Pollster":"A", "Date":"Feb 10 2010"},
                  {"ID":5, "State":"WA", "Pollster":"B", "Date":"Feb 10 2010"},
                  {"ID":6, "State":"WA", "Pollster":"B", "Date":"Mar 22 2010"}]
    
    
    print most_recent_poll_row(poll_rows1, "A", "SS") 
    print most_recent_poll_row(poll_rows1, "A", "WA") 
    """




    '\npoll_rows1 = [{"ID":1, "State":"WA", "Pollster":"A", "Date":"Jan 07 2010"},\n              {"ID":2, "State":"WA", "Pollster":"B", "Date":"Mar 21 2010"},\n              {"ID":3, "State":"WA", "Pollster":"A", "Date":"Jan 08 2010"},\n              {"ID":4, "State":"OR", "Pollster":"A", "Date":"Feb 10 2010"},\n              {"ID":5, "State":"WA", "Pollster":"B", "Date":"Feb 10 2010"},\n              {"ID":6, "State":"WA", "Pollster":"B", "Date":"Mar 22 2010"}]\n\n\nprint most_recent_poll_row(poll_rows1, "A", "SS") \nprint most_recent_poll_row(poll_rows1, "A", "WA") \n'




    ### Solution for Problem 3-1
    def unique_column_values(rows, column_name):
        """
        Given a list of rows and the name of a column (a string), returns a set
        containing all values in that column.
        """
        
        uniq=[]
        for row in rows:
            tmp=row[column_name]
            if tmp in uniq:
                pass
            else:
                uniq.append(row[column_name])
        return uniq



    ### Test for Problem 3-1
    """
    print unique_column_values(poll_rows1, "Pollster")
    print unique_column_values(poll_rows1, "State")
    """




    '\nprint unique_column_values(poll_rows1, "Pollster")\nprint unique_column_values(poll_rows1, "State")\n'




    ### Solution for Problem 3-2
    
    def pollster_predictions(poll_rows):
        """
        Given a list of poll data rows, returns pollster predictions.
        """
        pster=unique_column_values(poll_rows, "Pollster")
        state=unique_column_values(poll_rows, "State")
        thin=[]
        for p in pster:
            for s in state:
                thin.append(most_recent_poll_row(poll_rows, p, s))     
        #print thin        
        from collections import defaultdict
        prediction = defaultdict(dict)
        for t in thin:
            #print t
            if t =='None':
                pass
            else:
                state=t['State']
                edge=state_edges([t])[state]                #### Jesus, my 2 hours stuck on the "[]" !!!
                pster=t['Pollster']
                prediction[pster][state]=edge
        return prediction
    
        
        
        


    ### Test for Problem 3-2
    """
    rows4 = [
          {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
          {'State': 'WA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'}]
    rows3 = [
          {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
          {'State': 'CA', 'Dem': '2.1', 'Rep': '3.2', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'},
          {'State': 'CA', 'Dem': '2.1', 'Rep': '3.2', 'Date': 'Nov 06 2008', 'Pollster': 'PPP'},
          {'State': 'WA', 'Dem': '9.1', 'Rep': '7.1', 'Date': 'Nov 05 2008', 'Pollster': 'IPSOS'},
          {'State': 'CA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'IPSOS'}]
    
    pollster_predictions(rows3) ['PPP']
        #== {'PPP': {'WA': 0.9}}
    """




    "\nrows4 = [\n      {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},\n      {'State': 'WA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'}]\nrows3 = [\n      {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},\n      {'State': 'CA', 'Dem': '2.1', 'Rep': '3.2', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'},\n      {'State': 'CA', 'Dem': '2.1', 'Rep': '3.2', 'Date': 'Nov 06 2008', 'Pollster': 'PPP'},\n      {'State': 'WA', 'Dem': '9.1', 'Rep': '7.1', 'Date': 'Nov 05 2008', 'Pollster': 'IPSOS'},\n      {'State': 'CA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'IPSOS'}]\n\npollster_predictions(rows3) ['PPP']\n    #== {'PPP': {'WA': 0.9}}\n"




    ## Solution for problem 4-1
    def average_error(state_edges_predicted, state_edges_actual):
        """
        Given predicted state edges and actual state edges, returns
        the average error of the prediction.
        """
        sum=0
        for state in state_edges_predicted.iterkeys():            ### for keys, values in dict.iteritems():
            sum+=abs(state_edges_predicted[state]-state_edges_actual[state])
        return sum/len(state_edges_predicted)
            
        
        


    ## Test for problem 4-1
    """
    state_edges_pred_1 = {'WA': 1.0, 'CA': -2.3, 'ID': -20.1}
    state_edges_act_1 = {'WA': 2.1, 'CA': -1.4, 'ID': -19.1}
    average_error(state_edges_pred_1, state_edges_act_1)
    #assert average_error(state_edges_pred_1, state_edges_act_1) == 1.0
    """
    
    





    "\nstate_edges_pred_1 = {'WA': 1.0, 'CA': -2.3, 'ID': -20.1}\nstate_edges_act_1 = {'WA': 2.1, 'CA': -1.4, 'ID': -19.1}\naverage_error(state_edges_pred_1, state_edges_act_1)\n#assert average_error(state_edges_pred_1, state_edges_act_1) == 1.0\n"




    ## Solution for problem 4-2
    
    def pollster_errors(pollster_predictions, state_edges_actual):
        """
        Given pollster predictions and actual state edges, retuns pollster errors.
        """
        perrors={}
        for pster,precious in pollster_predictions.iteritems():
            perrors[pster]=average_error(precious,state_edges_actual)
        return perrors



    ## Test for problem 4-2
    
    """
    predictions = {
        'PPP': {'WA': 1.0, 'CA': -2.0, 'ID': -20.0},
        'ISPOP': {'WA': 2.0, 'ID': -19.0}
        }
    actual = {'WA': 2.0, 'CA': -1.0, 'ID': -19.0, 'OR': 2.2, 'DC': 0.1}
    print pollster_errors(predictions, actual)
    assert pollster_errors(predictions, actual) == {'PPP': 1.0, 'ISPOP': 0.0}
    
    """
    print 'x'

    x



    #### Solution for Problem 5
    
    def pivot_nested_dict(nested_dict):
        """
        Pivots a nested dictionary, producing a different nested dictionary
        containing the same values.
        The input is a dictionary d1 that maps from keys k1 to dictionaries d2,
        where d2 maps from keys k2 to values v.
        The output is a dictionary d3 that maps from keys k2 to dictionaries d4,
        where d4 maps from keys k1 to values v.
        For example:
          input = { "a" : { "x": 1, "y": 2 },
                    "b" : { "x": 3, "z": 4 } }
          output = {'y': {'a': 2},
                    'x': {'a': 1, 'b': 3},
                    'z': {'b': 4} }
        """
        
        d = {}
        for key, value in nested_dict.iteritems():    
            for ikey, ivalue in value.iteritems():
                d.setdefault(ikey,{})[key] = ivalue
        return d


    ### Test for Problem 5
    
    #def test_pivot_nested_dict():
    """
    us_wars_by_name = {
            "Revolutionary" : { "start": 1775, "end": 1783 },
            "Mexican" : { "start": 1846, "end": 1848 },
            "Civil" : { "start": 1861, "end": 1865 }
            }
    us_wars_by_start_and_end = {
            'start': {'Revolutionary': 1775, 'Civil': 1861, 'Mexican': 1846},
            'end': {'Revolutionary': 1783, 'Civil': 1865, 'Mexican': 1848}
            }
    print pivot_nested_dict(us_wars_by_name)
    
    assert pivot_nested_dict(us_wars_by_name) == us_wars_by_start_and_end
    """




    '\nus_wars_by_name = {\n        "Revolutionary" : { "start": 1775, "end": 1783 },\n        "Mexican" : { "start": 1846, "end": 1848 },\n        "Civil" : { "start": 1861, "end": 1865 }\n        }\nus_wars_by_start_and_end = {\n        \'start\': {\'Revolutionary\': 1775, \'Civil\': 1861, \'Mexican\': 1846},\n        \'end\': {\'Revolutionary\': 1783, \'Civil\': 1865, \'Mexican\': 1848}\n        }\nprint pivot_nested_dict(us_wars_by_name)\n\nassert pivot_nested_dict(us_wars_by_name) == us_wars_by_start_and_end\n'




    #### Solution for 6-1
    def average_error_to_weight(error):
        """
        Given the average error of a pollster, returns that pollster's weight.
        The error must be a positive number.
        """
        return error ** (-2)
    
    
    



    #### Test for 6-1
    """
    average_error_to_weight(.25)
    """




    '\naverage_error_to_weight(.25)\n'




    #### Solution for 6-2
    def weighted_average(items, weights):
        """
        Returns the weighted average of a list of items.
        
        Arguments:
        items is a list of numbers.
        weights is a list of numbers, whose sum is nonzero.
        
        Each weight in weights corresponds to the item in items at the same index.
        items and weights must be the same length.
        """
        assert len(items) > 0
        assert len(items) == len(weights)
        sumtop=0
        sumdw=0
        for a,b in zip(items, weights):
            sumtop+=a*b
            sumdw+=b
        return sumtop/sumdw
    
    



    #### Test for 6-2
    
    
    """
        assert weighted_average([3, 4, 5], [1, 1, 1]) == 4
        assert weighted_average([3, 4], [1, 1]) == 3.5
        assert weighted_average([2, 4, 4, 6], [1, 1, 1, 5]) == 5
        assert weighted_average([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]) == 3
        assert weighted_average([1, 2, 1], [3, 2, 5]) == 1.2
    """
    weighted_average([3, 4, 5], [1, 1, 1])
    weighted_average([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])




    3




    #### Solution for Problem 6-3
    DEFAULT_AVERAGE_ERROR = 5.0
    
    def pollster_to_weight(pollster, pollster_errors):
        """"
        Given a pollster and a pollster errors, return the given pollster's weight.
        """
        if pollster not in pollster_errors:
            weight = average_error_to_weight(DEFAULT_AVERAGE_ERROR)
        else:
            weight = average_error_to_weight(pollster_errors[pollster])
        return weight



    ### Test for Problem 6-3
    """
    def test_pollster_to_weight():
        pollster_errors = {"Gallup":4, "Rasmussen":10, "SurveyUSA":.25}
        assert pollster_to_weight("Gallup", pollster_errors) == 0.0625
        assert pollster_to_weight("SurveyUSA", pollster_errors) == 16
        assert pollster_to_weight("Google", pollster_errors) == 0.04
    
    pollster_errors = {"Gallup":4, "Rasmussen":10, "SurveyUSA":.25}
    pollster_to_weight("Gallup", pollster_errors)
    
    """




    '\ndef test_pollster_to_weight():\n    pollster_errors = {"Gallup":4, "Rasmussen":10, "SurveyUSA":.25}\n    assert pollster_to_weight("Gallup", pollster_errors) == 0.0625\n    assert pollster_to_weight("SurveyUSA", pollster_errors) == 16\n    assert pollster_to_weight("Google", pollster_errors) == 0.04\n\npollster_errors = {"Gallup":4, "Rasmussen":10, "SurveyUSA":.25}\npollster_to_weight("Gallup", pollster_errors)\n\n'




    ### Solution for 6-4
    def average_edge(pollster_edges, pollster_errors):
        """
        Given pollster edges and pollster errors, returns the average of these edges
        weighted by their respective pollster errors.
        """
        wt=[]
        for pster in pollster_edges.iterkeys():
            wt.append(pollster_to_weight(pster,pollster_errors))
        eg=[]
        for vl in pollster_edges.itervalues():
            eg.append(vl)
        return weighted_average(eg,wt)                           ### possible bugs: Does the same dict change the order of its items all the time.
    



    ### Test for 6-4
    """
    def test_average_edge():
        assert average_edge({"p1":3, "p2":4, "p3":5}, {"p1":1, "p2":1, "p3":1}) == 4
        assert average_edge({"p1":3, "p2":4, "p3":5}, {"p1":1, "p2":1, "p3":1, "p4":2, "p5": -8}) == 4
        assert average_edge({"p1":3, "p2":4}, {"p1":1, "p2":1}) == 3.5
        assert average_edge({"p1":2, "p2":4, "p3":4, "p4":6}, {"p1":1, "p2":1, "p3":1, "p4":5}) == 3.3684210526315788
        assert average_edge({"p1":1, "p2":2, "p3":3, "p4":4, "p5":5},
                            {"p1":1, "p2":2, "p3":3, "p4":4, "p5":5}) == 1.560068324160182
        assert average_edge({"p1":3, "p2":4, "p3":5}, {"p1":5, "p2":5}) == 4
        assert average_edge({"p1":3, "p2":4, "p3":5}, {}) == 4
    """
    
        
    average_edge({"p1":3, "p2":4, "p3":5}, {"p1":1, "p2":1, "p3":1, "p4":2, "p5": -8})
    average_edge({"p1":1, "p2":2, "p3":3, "p4":4, "p5":5},
                            {"p1":1, "p2":2, "p3":3, "p4":4, "p5":5})
    average_edge({"p1":2, "p2":4, "p3":4, "p4":6}, {"p1":1, "p2":1, "p3":1, "p4":5})
    
    





    3.3684210526315788




    #### Solution for 7
    
    def predict_state_edges(pollster_predictions, pollster_errors):
        """
        Given pollster predictions from a current election and pollster errors from
        a past election, returns the predicted state edges of the current election.
        """
        pollster_predictions=pivot_nested_dict(pollster_predictions)
        magic={}
        for k,v in pollster_predictions.iteritems():
            magic[k]=average_edge(v,pollster_errors)
        return magic



    #### Test for 7
    
    """
    def test_predict_state_edges():
        pollster_predictions = {
          'PPP': { 'WA': -11.2, 'CA': -2.0, 'ID': -1.1 },
          'IPSOS': { 'WA': -8.7, 'CA': -3.1, 'ID': 4.0 },
          'SurveyUSA': { 'WA': -9.0, 'FL': 0.5 },
          }
        pollster_errors = {'PPP': 1.2, 'IPSOS': 4.0, 'SurveyUSA':3.5, 'NonExistant':100.0}
        assert predict_state_edges(pollster_predictions, pollster_errors) == {'CA':
        -2.0908256880733944, 'FL': 0.5, 'ID': -0.6788990825688075, 'WA': -10.799509886766941}
    
    ### Test begins here:
    pollster_predictions = {
          'PPP': { 'WA': -11.2, 'CA': -2.0, 'ID': -1.1 },
          'IPSOS': { 'WA': -8.7, 'CA': -3.1, 'ID': 4.0 },
          'SurveyUSA': { 'WA': -9.0, 'FL': 0.5 },
          }
    pollster_errors = {'PPP': 1.2, 'IPSOS': 4.0, 'SurveyUSA':3.5, 'NonExistant':100.0}
    predict_state_edges(pollster_predictions, pollster_errors) 
    """
    
    print 'x'

    x



    ####The Main function
    
    def electoral_college_outcome(ec_rows, state_edges):
        """
        Given electoral college rows and state edges, returns the outcome of
        the Electoral College, as a map from "Dem" or "Rep" to a number of
        electoral votes won.  If a state has an edge of exactly 0.0, its votes
        are evenly divided between both parties.
        """
        ec_votes = {}               # maps from state to number of electoral votes
        for row in ec_rows:
            ec_votes[row["State"]] = float(row["Electors"])
    
        outcome = {"Dem": 0, "Rep": 0}
        for state in state_edges:
            votes = ec_votes[state]
            if state_edges[state] > 0:
                outcome["Dem"] += votes
            elif state_edges[state] < 0:
                outcome["Rep"] += votes
            else:
                outcome["Dem"] += votes/2.0
                outcome["Rep"] += votes/2.0
        return outcome
    
    def print_dict(dictionary):
        """
        Given a dictionary, prints its contents in sorted order by key.
        Rounds float values to 8 decimal places.
        """
        for key in sorted(dictionary.keys()):
            value = dictionary[key]
            if type(value) == float:
                value = round(value, 8)
            print key, value
    
    def main():
        """
        Main function, which is executed when election.py is run as a Python script.
        """
        # Read state edges from the 2008 election
        edges_2008 = state_edges(read_csv("data/2008-results.csv"))
    
        # Read pollster predictions from the 2008 and 2012 election
        polls_2008 = pollster_predictions(read_csv("data/2008-polls.csv"))
        polls_2012 = pollster_predictions(read_csv("data/2012-polls.csv"))
       
        # Compute pollster errors for the 2008 election
        error_2008 = pollster_errors(polls_2008, edges_2008)
    
        # Predict the 2012 state edges
        prediction_2012 = predict_state_edges(polls_2012, error_2008)
    
        # Obtain the 2012 Electoral College outcome
        ec_2012 = electoral_college_outcome(read_csv("data/2012-electoral-college.csv"),
                                            prediction_2012)
    
        print "Predicted 2012 election results:"
        print_dict(prediction_2012)
        print
    
        print "Predicted 2012 Electoral College outcome:"
        print_dict(ec_2012)
        print
    main()

    Predicted 2012 election results:
    AK -22.0
    AL -18.0
    AR -24.122398
    AZ -4.66430118
    CA 14.11583444
    CO 1.20293566
    CT 12.84410977
    DC 80.0
    DE 25.0
    FL 0.57143612
    GA -9.30541301
    HI 27.0
    IA 2.15816992
    ID -36.0
    IL 19.04412837
    IN -9.47132082
    KS -20.0
    KY -14.0
    LA -11.63974839
    MA 20.61154303
    MD 23.44739426
    ME 13.07697933
    MI 6.21542005
    MN 7.88152447
    MO -9.20776204
    MS -6.0
    MT -8.60944804
    NC -1.08747954
    ND -17.24462124
    NE -14.70698124
    NH 1.49398848
    NJ 12.1577076
    NM 9.90780976
    NV 2.949298
    NY 26.72006693
    OH 3.82265211
    OK -25.0
    OR 6.08883386
    PA 4.47316823
    RI 19.37311842
    SC -6.0
    SD -9.0
    TN -9.86945113
    TX -15.81828931
    UT -45.24755722
    VA 3.45068238
    VT 37.0
    WA 15.28608023
    WI 7.49682045
    WV -14.0
    WY -32.0
    
    Predicted 2012 Electoral College outcome:
    Dem 332.0
    Rep 206.0
    



    #### Test the Main function
    
    

