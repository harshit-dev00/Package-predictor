// lib/model_prediction.dart
class PredictionResponse {
  final double predictedPackage;

  PredictionResponse({required this.predictedPackage});

  factory PredictionResponse.fromJson(Map<String, dynamic> json) {
    return PredictionResponse(
      predictedPackage: json['predicted_package'],
    );
  }
}
