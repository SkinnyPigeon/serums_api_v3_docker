# Serums data lake setup - Linux file system

import os

# Setting up the use case partners

hospital_names = ["ustan", "fcrb", "zmc"]

# Setting up RIF routes

def rif_routes(hospital_name):
    rif_results = []
    base = '/datalake/{}/000-RIF'.format(hospital_name)
    
# 100-Functional-Layer
    group = '100-Functional-Layer'
    end = ['100-Retrieve', '200-Assess', '300-Process', '400-Transform', '500-Organize', '600-Report']
    for x in range(0, len(end)):
        concatenated_route = base + '/' + group + '/' + end[x] + '/'
        rif_results.append(concatenated_route)

# 200-Operational-Management-Layer
    group = '200-Operational-Management-Layer'
    sub = '100-Crawler-Definitions'
    end = ['100-Crawler-Master-Service-Definitions', 
        '200-Crawler-Workcell-Service-Definitions', 
        '300-Crawler-Input-Definitions', 
        '400-Crawler-Output-Definitions']

    for x in range(0, len(end)):
        concatenated_route = base + '/' + group + '/' + sub + '/' + end[x] + '/'
        rif_results.append(concatenated_route)

    sub = '200-Crawler-Management'
    end = ['100-Retrieve-Population',
        '200-Assess-Population',
        '300-Process-Population',
        '400-Transform-Population',
        '500-Organise-Population',
        '600-Report-Population']

    for x in range(0, len(end)):
        concatenated_route = base + '/' + group + '/' + sub + '/' + end[x] + '/'
        rif_results.append(concatenated_route)
    
    sub = ['300-Parameters',
       '400-Scheduling',
       '500-Monitoring',
       '600-Communication',
       '700-Alerting',
       '800-Codes-Management']

    for x in range(0, len(sub)):
        concatenated_route = base + '/' + group + '/' + sub[x] + '/'
        rif_results.append(concatenated_route)

# 300-Audit-Balance-Control-Layer

    group = '300-Audit-Balance-Control-Layer'
    sub = ['100-Audit',
        '200-Balance',
        '300-Control']

    for x in range(0, len(sub)):
        concatenated_route = base + '/' + group + '/' + sub[x] + '/'
        rif_results.append(concatenated_route)

# 400-Utility-Layer

    group = '400-Utility-Layer'
    sub = ['100-Maintenance-Utilities',
        '200-Data-Utilities',
        '300-Processing-Utilities']

    for x in range(0, len(sub)):
        concatenated_route = base + '/' + group + '/' + sub[x] + '/'
        rif_results.append(concatenated_route)

# 500-Business-Layer

    group = '500-Business-Layer'
    sub = ['100-Functional-Requirements',
        '200-Non-functional-Requirements',
        '300-Data-Profiles',
        '400-Sun-Models']

    for x in range(0, len(sub)):
        concatenated_route = base + '/' + group + '/' + sub[x] + '/'
        rif_results.append(concatenated_route)

# Return results 
    return rif_results

###############################################

# Setting up Data Lake routes

def dl_routes(hospital_name):
    dl_results = []
    base = '/datalake/{}/100-DL'.format(hospital_name)

# 000-Workspace-Zone

    group = '000-Workspace-Zone'

    concatenated_route = base + '/' + group + '/'
    dl_results.append(concatenated_route)

# 100-Raw-Zone

    group = '100-Raw-Zone'
    sub = '100-External'
    end = ['100-University-of-St-Andrews',
        '200-Zuyderland-Medisch-Centrum',
        '300-Fundacio-Clinic',
        '900-Other']
    
    for x in range(0, len(end)):
        concatenated_route = base + '/' + group + '/' + sub + '/' + end[x] + '/'
        dl_results.append(concatenated_route)

    sub = '200-Internal'
    end = ['100-CSV',
        '200-TEXT',
        '300-JSON',
        '400-XML',
        '900-Human-in-the-Loop']

    for x in range(0, len(end)):
        concatenated_route = base + '/' + group + '/' + sub + '/' + end[x] + '/'
        dl_results.append(concatenated_route)

    sub = '300-Archive'
    end = ['100-CSV',
        '200-TEXT',
        '300-JSON',
        '400-XML',
        '900-Human-in-the-Loop']

    for x in range(0, len(end)):
        concatenated_route = base + '/' + group + '/' + sub + '/' + end[x] + '/'
        dl_results.append(concatenated_route)

# 200-Structured-Zone

    group = '200-Structured-Zone'
    
    concatenated_route = base + '/' + group + '/'
    dl_results.append(concatenated_route)

# 300-Curated-Zone

    group = '300-Curated-Zone'
    dv = ['Hub','Satellite','Link']
    tpole = ['Time','Person','Object','Location','Event']

    for dvpath in dv:    
        if dvpath == 'Link':        
            for hubpath1 in tpole:
                for hubpath2 in tpole:
                    if hubpath1 != hubpath2:
                        hubpath = hubpath1 + '-' + hubpath2
                        concatenated_route = base + '/' + group + '/' + dvpath + '/' + hubpath + '/'
                        dl_results.append(concatenated_route)
        else:
            for hubpath in tpole:
                concatenated_route = base + '/' + group + '/' + dvpath + '/' + hubpath + '/'
                dl_results.append(concatenated_route)

# 400-Consumer-Zone

    group = '400-Consumer-Zone'

    concatenated_route = base + '/' + group + '/'
    dl_results.append(concatenated_route)

# 500-Analytics-Zone

    group = '500-Analytics-Zone'

    concatenated_route = base + '/' + group + '/'
    dl_results.append(concatenated_route)

    return dl_results

# Making the DL

for hospital_name in hospital_names:
    rif_results = rif_routes(hospital_name)
    for route in rif_results:
       os.system("mkdir -p {}".format(route))

for hospital_name in hospital_names:
    dl_results = dl_routes(hospital_name)
    for route in dl_results:
       os.system("mkdir -p {}".format(route))
