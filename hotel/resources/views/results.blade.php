<!-- resources/views/results.blade.php -->

@extends('layouts.app')

@section('content')
    <div class="container">
        <h1>Prediction Results</h1>

        @if ($prediction)
            <p>The prediction is: {{ $prediction }}</p>
        @else
            <p>Failed to make a prediction.</p>
        @endif
    </div>
@endsection
