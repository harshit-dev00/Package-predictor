import 'package:flutter/material.dart';
import 'prediction_screen.dart'; 

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Package Predictor',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: PredictionScreen(),
    );
  }
}
