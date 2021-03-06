<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>遥控机械狗</title>
    <link href="/static/css/bootstrap.min.css" rel="stylesheet" media="screen"->
    <script src="/static/js/jquery.js"></script>
    <style type="text/css">
        #up {
            margin-left: 55px;
            margin-bottom: 3px;
        }
        #down {
            margin-top: 3px;
            margin-left: 55px;
        }
    </style>
    <script>
        $(function(){
            $("button").click(function(){
                $.post("/cmd",this.id,function(data,status){});
            });
        });

    </script>
</head>
<body>
<div>
<h2>机械狗遥控器</h2>
<div id="container" class="container">   
    <div>
        <button id="up" class="btn btn-lg btn-primary glyphicon glyphicon-circle-arrow-up"></button>
    </div>
    <div>
        <button id='left' class="btn btn-lg btn-primary glyphicon glyphicon-circle-arrow-left"></button>
        <button id='stop' class="btn btn-lg btn-primary glyphicon glyphicon-stop"></button>
        <button id='right' class="btn btn-lg btn-primary glyphicon glyphicon-circle-arrow-right"></button>
    </div>
    <div>
        <button id='down' class="btn btn-lg btn-primary glyphicon glyphicon-circle-arrow-down"></button>
    </div>    
</div>
</div>

<script src="/static/js/bootstrap.min.js"></script>
</body>
</html>