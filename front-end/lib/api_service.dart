import 'dart:convert';
import 'package:http/http.dart' as http;
import 'model_prediction.dart';

class ApiService {
  final String baseUrl = "http://10.0.2.2:8000"; // Android emulator localhost

  Future<PredictionResponse> getPrediction(double cgpa) async {
    final url = Uri.parse("$baseUrl/predict");

    final response = await http.post(
      url,
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"cgpa": cgpa}),
    );

    if (response.statusCode == 200) {
      return PredictionResponse.fromJson(jsonDecode(response.body));
    } else {
      throw Exception("Failed to get prediction");
    }
  }
}
