#!/bin/bash
echo "Content-type: text/html"
echo ''
echo 'CGI Bash Example'
echo "<html><head><title>bash</title>"
echo "<link rel='stylesheet' type='text/css' href='http://netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap.min.css'>"
echo "<style>body{color:red; background-color: #111}</style></head><body>"
echo '<form class="col-lg-12">
            <div class="input-group" style="width:340px;text-align:center;margin:0 auto;">'
echo "<input class='form-control input-lg' title='Do not worry. We hate spam, and will not share your email with anyone.' placeholder='Enter your email address' type='text'></div></form>"
octave program.m >wanted.out
echo "</body></html>"
