brand=" "
model = " "

def get_intent(data):
    global brand , model
    m=data['message'].lower()
    if data['key']=='name':
        return "brand"
    elif data['key']=='brand':
        brand = m
        if m in ['redmi','samsung','realme','oppo','vivo']:
            return 'redmi'
        else:
            return m
        
    elif data['key']=='mobiles':
        model = m
        if any(x in m for x in ['model1','model2','model3']):
            return 'response'
        else:
            return m
        
    elif data['key']=='thanks':
        if any(x in m for x in ['ok','tq','kk','k','thanks','thank u','thank you']):
            return 'thank'
        else:
            return m
    else:
        return m


def handle(data):
    global brand, model
    from flask import render_template
    intent=get_intent(data)
    if intent=='redmi':
        return render_template('messages/redmi.html',question={'key':'mobiles','text':'available models are : 👇'},options={'tasks':[
        {'key':'model1','description':'price less than 10,000Rs'},
        {'key':'model2','description':'price between 10,000Rs and 20,000Rs'},
        {'key':'model3','description':'price greater than 20,000Rs'}] })
    elif intent=='response':
        from .data.about import bot
        return render_template('messages/response.html',data=bot,brand=brand,model=model,question={'key':'thanks','text':'great u made a great selection.. ur desired mobile is available..🤩'})
    elif intent=='thank':
        return render_template('messages/thank.html',question={'key':'finish','text':'thank you for chatting..🎅 hope u will reach out to our store..🤗'})
    elif intent=="brand":
        return render_template('messages/brand.html',data=data['message'],question={'key':'brand','text':'what brand u like..'})
    else:
        return render_template('messages/error.html',data=intent,question={'key':'brand','text':intent})
