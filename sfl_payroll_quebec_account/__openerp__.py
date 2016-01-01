# -*- coding:utf-8 -*-
##############################################################################
#
#    Copyright (C) 2010 - 2016 Savoir-faire Linux. All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Quebec - Payroll Accounting',
    'category': 'Localization',
    'version': '8.0.1.0.0',
    'license': 'AGPL-3',
    'author': "Savoir-faire Linux",
    'website': 'http:/www.savoirfairelinux.com/',
    'depends': [
        'sfl_payroll_quebec',
        'sfl_payroll_canada_account',
    ],
    'data': [
        'views/hr_releve_1_summary.xml',
        'views/res_company.xml',
        'data/hr_salary_rule.xml',
        'data/res_company.xml',
    ],
    'test': [],
    'installable': True,
}
