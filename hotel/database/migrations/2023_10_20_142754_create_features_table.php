<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('features', function (Blueprint $table) {
            $table->id();
            $table->string('hotel')->nullable();
            $table->string('days_in_waiting_list')->nullable();
            $table->string('agent_involved')->nullable();
            $table->string('reserved_is_assigned')->nullable();
            $table->string('has_special_requests')->nullable();
            $table->string('customer_type')->nullable();
            $table->string('deposit_type')->nullable();
            $table->string('is_repeated_guest')->nullable();
            $table->string('distribution_channel')->nullable();
            $table->string('market_segment')->nullable ();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('features');
    }
};
