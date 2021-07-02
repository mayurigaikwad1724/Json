import json
def is_complex_num(object):
    if '__complex__' in object:
        return complex(object["real"],object['img'])
    return object

complex_object=json.loads('{"__complex_": true,"real":4,"img":5}',object_hook=is_complex_num)
simple_object=json.loads('{"real":4,"img":3}',object_hook=is_complex_num)
print("complex_object: ",complex_object)
print("without complex object: ",simple_object)