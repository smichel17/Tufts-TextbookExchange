<!DOCTYPE html>
<html>
    <head>
        <title>Textbook Results</title>

        <link href='./styles/base.css' type='text/css' rel='stylesheet' />
        <link href='./styles/layout.css' type='text/css' rel='stylesheet' />
        <link href='./styles/skeleton.css' type='text/css' rel='stylesheet' />
    </head>
    <body>
        <div class="super-container full-width">
            <div class="container">         
                <header>
                    <div class="sixteen columns">
                        <div class="eight columns alpha">
                            <h1 id="logo" style="margin-top: 20px; margin-bottom: 10px;">
                                <a href="index.html"><img src="images/logo.png" alt="logo" /></a>
                            </h1>
                        </div>
                    </div>
                </header>
                <hr class="large" style="margin:10px;">
            </div>
        </div>
        <div class="container">
            <div class="three columns sidebar">
                <nav>
                    <ul>
                        <li><strong><a href="/buy">Buy Textbooks</a></strong></li>
                        <li><strong><a href="/sell">Sell Textbooks</a></strong></li>
                        <li><strong><a href="/about">About TextEx</a></strong></li>

                    </ul>
                </nav>
            </div>

            <div class="container">
            <div class="four columns">
                <form method="POST" action="/results">

                    <table>
                        <th>Department</th><th>Course</th><th>Price</th><th>Description</th><th></th>
                            %for row in rows:
                             <tr>
                                <td>{{row[1]}}</td>
                                <td>{{row[2]}}</td>
                                <td>{{row[3]}}</td>
                                <td>{{row[4]}}</td>
                                <td><button name='button' value={{row[0]}} type="submit">BUY</button></td>
                             </tr>
                            %end

                    </table>

                    
                </form>
            </div>
            </div>
        </div>
    </body>
</html>