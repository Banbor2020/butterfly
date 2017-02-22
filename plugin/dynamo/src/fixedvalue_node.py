# assign inputs
_value = IN[0]
fixedValue = None

try:
    from butterfly.fields import FixedValue
except ImportError as e:
    msg = '\nFailed to import butterfly. Did you install butterfly on your machine?' + \
            '\nYou can download the installer file from github: ' + \
            'https://github.com/mostaphaRoudsari/Butterfly/tree/master/plugin/dynamo/samplefiles' + \
            '\nOpen an issue on github if you think this is a bug:' + \
            ' https://github.com/mostaphaRoudsari/Butterfly/issues'
        
    raise ImportError('{}\n{}'.format(msg, e))

if _value:
    fixedValue = FixedValue(_value)

# assign outputs to OUT
OUT = (fixedValue,)