from django.shortcuts import render , redirect

# Create your views here.
def temp_convertor(request):
    if request.method == 'POST':
        temperature = request.POST.get('temp')
        temperature_scale = request.POST.get('unit')
        if not temperature and not temperature_scale:
            context={
                'title': 'Temperature Convertor',
                'temp_error': 'Please enter your temperature',
                'scale_error': 'Please enter your temperature scale'
            }
            return render(request, 'temperature.html', context)

        elif not temperature:
            context={
                'title': 'Temperature Convertor',
                'temp_error': 'Please enter your temperature',
            }
            return render(request, 'temperature.html', context)
        elif not temperature_scale:
            context={
                'title': 'Temperature Convertor',
                'scale_error': 'Please select your temperature scale'
            }
            return render(request, 'temperature.html', context)
        else:
            try:

                    temperature = float(temperature)
                    if temperature_scale == 'Celsius':
                        Celsius = temperature
                        # Convert to Fahrenheit
                        Fahrenheit = (temperature * 9/5) + 32 
                        # Convert to Kelvin
                        Kelvin = temperature + 273.15


                    elif temperature_scale == 'Fahrenheit':
                        Fahrenheit = temperature
                        # Fahrenheit To Celsius
                        Celsius = (temperature - 32) * 5/9
                        # Fahrenheit To Kelvin
                        #  C = (fahrenheit - freez_of_F)*5/9
                        Kelvin =( (temperature - 32 )*5/9) + 273.15


                    elif temperature_scale == 'Kelvin':
                        Kelvin = temperature
                        # Convert to Celsius
                        Celsius = temperature - 273.15
                        # Convert to Fahrenheit
                        # F = ((K - 273.15)*9/5) + 32
                        Fahrenheit =((temperature - 273.15)*9/5) + 32
                    context = {
                            'title': 'Temperature Convertor',
                            'Celsius': round(Celsius, 2),
                            'Fahrenheit': round(Fahrenheit, 2),
                            'Kelvin': round(Kelvin, 2),
                            'temperature_scale': temperature_scale,
                        }
                    return render(request, 'temperature.html', context)
            except ValueError:
                context = {
                    'title': 'Temperature Convertor',
                    'temp_error': 'Please enter a valid temperature value',
                }
                return render(request, 'temperature.html', context)
                
    return render(request, 'temperature.html', {'title': 'Temperature Convertor'})


def temp_convertor_reload(request):
    return redirect('temp_convertor')  