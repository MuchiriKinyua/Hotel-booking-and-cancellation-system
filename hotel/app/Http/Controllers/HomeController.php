<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Models\Features;

class HomeController extends Controller
{
    public function index()
    {
        return view('home.index');
    }
    public function upload(Request $request)
    {
        $data=new Features;

        $data->hotel=$request->hotel;
        $data->days_in_waiting_list=$request->days_in_waiting_list;
        $data->agent_involved=$request->agent_involved;
        $data->reserved_is_assigned=$request->reserved_is_assigned;
        $data->has_special_requests=$request->has_special_requests;
        $data->customer_type=$request->customer_type;
        $data->deposit_type=$request->deposit_type;
        $data->is_repeated_guest=$request->is_repeated_guest;
        $data->distribution_channel=$request->distribution_channel;
        $data->market_segment=$request->market_segment;

        $data->save();

        return redirect()->back();
    }
}
