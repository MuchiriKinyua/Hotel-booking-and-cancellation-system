<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" type="text/css" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.0/css/all.min.css">

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

    <!-- Latest compiled and minified JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <title>Hotel system</title>
</head>
<body>
    <nav>
        <label>HOTEL BOOKING AND CANCELLATION SYSTEM</label>
        <ul>

            @if (Route::has('login'))

                @auth
                <li>
                    <a href="{{ url('/dashboard') }}" class="btn btn-success">{{ Auth::user()->name }}</a>
                </li>

                @else

            <li>
                <a href="{{ route('register') }}" class="btn btn-success">Register</a>
            </li>

            <li>
                <a href="{{ route('login') }}" class="btn btn-primary">Login</a>
            </li>

            @endauth

            @endif

        </ul>
    </nav>
    <div class="dev_design">
        <p>The global hotel industry, pivotal in the tourism sector, faces challenges in an evolving landscape. Online reservations have surged due to convenience, options and flexibility.</p>
        <img src="Hotel booking.jpg" alt="">
        <img src="Hotel cancellation.webp" alt="">
        <p>This predictive model developed enhances revenue stability by recognizing seasonal trends, analyzing waiting times, and enabling personalized loyalty programs.</p>
        <div class="copyright">
            <p>Copyright &copy; Made with <i class="fas fa-heart"></i> by MuchiriKinyua. All rights reserved.</p>
        </div>
    </div>
</body>
</html>
