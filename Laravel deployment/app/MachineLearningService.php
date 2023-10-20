<?php
// app/MachineLearningService.php

namespace App;

use joblib;

use Illuminate\Support\Facades\Storage;
use Illuminate\Support\Facades\Log;

class MachineLearningService
{
    public function loadGradientBoostModel()
    {
        // Load the Gradient Boosting model
        try {
            $command = "python load_model.py";
            $output = exec($command);
            return $output; // This should be the model object
        } catch (\Exception $e) {
            Log::error('Failed to load the Gradient Boosting model: ' . $e->getMessage());
            return null;
        }
    }


    public function loadKerasModel()
    {
        // Load the Keras model
        try {
            $modelPath = storage_path('models/keras_model.h5');
            // Load your Keras model using the appropriate library
            // Replace the following line with your actual code to load the model
            $model = load_keras_model($modelPath);
            return $model;
        } catch (\Exception $e) {
            Log::error('Failed to load the Keras model: ' . $e->getMessage());
            return null;
        }
    }

    public function makeGradientBoostPrediction($features)
    {
        $model = $this->loadGradientBoostModel();
        if ($model) {
            // Make predictions using the loaded model
            return $model->predict($features);
        }
        return null;
    }

    public function makeKerasPrediction($features)
    {
        $model = $this->loadKerasModel();
        if ($model) {
            // Make predictions using the loaded model
            return $model->predict($features);
        }
        return null;
    }
}
