from django.contrib import admin
from .models import DisasterIndex
# Register your models here.
class DisasterIndexAdmin(admin.ModelAdmin):
    list_display = ('id','district','vdc','wardno','incidentplace','incidentdate','incidenttype','deathmale','deathfemale','deathunknown','totaldeath','missingpeople','affectedfamily','estimatedloss','injured','govthousesfullydamaged','govthousespartiallydamaged','displacedmale','displacedfemale','propertyloss','noofdisplacedfamily','cattlesloss','displacedshed','source','remarks')
    list_filter = ['incidentdate', 'incidenttype']
    date_hierarchy = 'incidentdate'
    empty_value_display = '-empty-'
    
    

admin.site.register(DisasterIndex, DisasterIndexAdmin)