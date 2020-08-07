from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import Show

# Create your views here.



def allShows(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)


def addingShow(request):
    return render(request, "new.html")


def realAddingShow(request):
    # just for debugging
    print(request.POST)

    #validation errors addingShow Post Data###
    # creating a variable errors 
    # assigning it the result of invocking the 
    # #basic_validator method with reqeust.POST object
    errors = Show.objects.basic_validator(request.POST)
    
    # we are checking to see  if thereis anything 
    # in the erros diction.
    if len(errors) > 0:
        for key, value in errors.items():
            #by calling the error function
            #we'll have acces to the erros we set
            # on the next request
            messages.error(request, value)
        # redirect the user back to the form to fix the errors 
        #this is prompting another request
        return redirect('/shows/new')

    else:

        newShow = Show.objects.create(
        title = request.POST['titleLabel'],
        network = request.POST['networkLabel'],
        release_date = request.POST['releaseDateLabel'],
        description = request.POST['descriptionLabel']
    )
    
    return redirect(f'/shows/{newShow.id}')




#showing show information on the html 
def showShow(request, id):
    context = {
         'this_show' : Show.objects.get(id=id)
    }
    return render(request, "show_info.html", context)




def editingShowPage (request, id2):
    current_show = Show.objects.get(id=id2)
#   current_show.release_date = current_show.release_date.strftime("%Y-%m-%d")    
    context = {
        'this_show' : Show.objects.get(id=id2), #creating context to pass to html template
    }                                  #the variable template will be calle this_movie
    return render(request, "edit_show.html", context)
    # returns an instance of HttpResponse


def updatingShow (request, id3): #id3 coming from url:id3 
    errors = Show.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(request.META.get('HTTP_REFERER')) #return an instance of HttpResponse

    else:
        updatedShow = Show.objects.get(id=id3)

        updatedShow.title = request.POST['titleLabel']
        updatedShow.network = request.POST['networkLabel']
        updatedShow.release_date = request.POST['releaseDateLabel']
        updatedShow.description = request.POST['descriptionLabel']

        updatedShow.save()

        return redirect (f"/shows/{updatedShow.id}")


def destroyingShow(request, id4):
        show_to_be_destroyed = Show.objects.get(id=id4)
        show_to_be_destroyed.delete()

        return redirect ("/shows")

def index(request):  #changed from index to dashboard
    
    return redirect("/")

