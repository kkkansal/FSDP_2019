# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 03:25:02 2019

@author: kunal
"""

import json
json_string="""
{
	"faculty": [{
			"First_name": "Ajay kumar",
			"Last_name": "Sharma",
			"Department": "Computer Science",
			"Research_areas": ["Statistics", "Probability"],
			"contact_details": {
				"mobile_no": "88965742",
				"E-mail_id": "ajaykumar88@gmail.com"
			}

		},

		{
			"First_name": "vijay kumar",
			"Last_name": "verma",
			"Department": "Computer Science",
			"Research_areas": ["Toc", "DSM"],
			"contact_details": [{
				"mobile_no": "999965742",
				"E-mail_id": "vijaykumar1188@gmail.com"
			}]

		}
	]
}
"""