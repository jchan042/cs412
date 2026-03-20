# File: views.py
# Author: Jocelyn Chan (jchan042@bu.edu) 3/18/2026
# Description: Returns an HTML template view for each URL 

from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from .models import Voter
import plotly
import plotly.graph_objs as go

# Voter classes

# Displays voter info in a list 
class VotersListView(ListView):
    '''View to display voter results'''
    
    model = Voter
    template_name = 'voter_analytics/voters.html'   
    context_object_name = 'voters'
    paginate_by = 100 # displays 100 voters per page 
    
    # used to filter results 
    def get_queryset(self):
        results = super().get_queryset()
        
        # look for URL params to filter by 
        if self.request.GET.get('party_affiliation'):
            results = results.filter(party=self.request.GET.get('party_affiliation'))

        if self.request.GET.get('min_dob'):
            results = results.filter(dob__year__gte=self.request.GET.get('min_dob'))

        if self.request.GET.get('max_dob'):
            results = results.filter(dob__year__lte=self.request.GET.get('max_dob'))

        if self.request.GET.get('voter_score'):
            results = results.filter(voter_score=self.request.GET.get('voter_score'))

        # election filters
        if self.request.GET.get('v20'):
            results = results.filter(v20=True)

        if self.request.GET.get('v21_town'):
            results = results.filter(v21_town=True)

        if self.request.GET.get('v21_primary'):
            results = results.filter(v21_primary=True)

        if self.request.GET.get('v22_general'):
            results = results.filter(v22_general=True)

        if self.request.GET.get('v23'):
            results = results.filter(v23=True)
        
        return results
    
    # used to keep form values selected after search
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['party_affiliation'] = self.request.GET.get('party_affiliation', '')
        context['min_dob'] = self.request.GET.get('min_dob', '')
        context['max_dob'] = self.request.GET.get('max_dob', '')
        context['voter_score'] = self.request.GET.get('voter_score', '')
        context['v20_checked'] = self.request.GET.get('v20', '')
        context['v21_town_checked'] = self.request.GET.get('v21_town', '')
        context['v21_primary_checked'] = self.request.GET.get('v21_primary', '')
        context['v22_general_checked'] = self.request.GET.get('v22_general', '')
        context['v23_checked'] = self.request.GET.get('v23', '')
        context['form_action'] = reverse('voters') # for the filtering form
        return context
    
    
# Displays a single voter information view 
class VoterDetailView(DetailView):
    '''View to display one voter information'''
    
    template_name = 'voter_analytics/voter.html'
    model = Voter
    context_object_name = 'voter' # singular
    

# Graphs 

# Displays a list of graphs for aggregate data 
class GraphsListView(VotersListView): 
    '''View to display mulitple graphs'''
    
    template_name = 'voter_analytics/graphs.html'
    context_object_name = 'voters'
    paginate_by = None
    
    # override this method to create graphs 
    def get_context_data(self, **kwargs):
        '''
        Provide context variables for use in template
        '''
        # superclass context
        context = super().get_context_data(**kwargs)
        voters = context['voters']
        
        # total number of voters in current result set
        n = len(voters)
        
        # histogram of voters by dob year 
        birth_year_counts = {}
        for voter in voters:
            year = voter.dob.year
            if year in birth_year_counts:
                birth_year_counts[year] += 1
            else:
                birth_year_counts[year] = 1

        x_birth = sorted(birth_year_counts.keys())
        y_birth = [birth_year_counts[year] for year in x_birth]

        fig_birth = go.Bar(x=x_birth, y=y_birth)
        title_text = f"Distribution of Voters by Year of Birth (n={n})"

        graph_div_birth = plotly.offline.plot(
            {
                "data": [fig_birth],
                "layout_title_text": title_text,
            },
            auto_open=False,
            output_type="div"
        )

        # return div as template context var 
        context['graph_div_birth'] = graph_div_birth
        
        
        # pie chart of voters by party affiliation
        party_counts = {}
        for voter in voters:
            party = voter.party
            if party in party_counts:
                party_counts[party] += 1
            else:
                party_counts[party] = 1

        x_party = list(party_counts.keys())
        y_party = list(party_counts.values())

        fig_party = go.Pie(labels=x_party, values=y_party)
        title_text = f"Distribution of Voters by Party Affiliation (n={n})"

        graph_div_party = plotly.offline.plot(
            {
                "data": [fig_party],
                "layout_title_text": title_text,
            },
            auto_open=False,
            output_type="div"
        )

        context['graph_div_party'] = graph_div_party
        
        
        # histogram of voter participation in each election
        election_labels = ['v20state', 'v21town', 'v21primary', 'v22general', 'v23town']
        election_counts = [0, 0, 0, 0, 0]

        for voter in voters:
            if voter.v20:
                election_counts[0] += 1
            if voter.v21_town:
                election_counts[1] += 1
            if voter.v21_primary:
                election_counts[2] += 1
            if voter.v22_general:
                election_counts[3] += 1
            if voter.v23:
                election_counts[4] += 1

        fig_elections = go.Bar(x=election_labels, y=election_counts)
        title_text = f"Voter Participation in Each Election (n={n})"

        graph_div_elections = plotly.offline.plot(
            {
                "data": [fig_elections],
                "layout_title_text": title_text,
            },
            auto_open=False,
            output_type="div"
        )

        context['graph_div_elections'] = graph_div_elections
        context['form_action'] = reverse('graphs')
        
        return context
        
    
        