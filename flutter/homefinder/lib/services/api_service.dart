import 'package:http/http.dart' as http;

class ApiService {
  static Future<http.Response> generateAmortizationReport({
    required String principal,
    required String extraPayment,
    required String mortgageAmount,
    required String interestRate,
  }) async {
    final url = Uri.http(
      'localhost:5000',
      '/api/v1/generateAmortizationReport',
      {
        'principal': principal,
        'extraPayment': extraPayment,
        'mortgageAmount': mortgageAmount,
        'interestRate': interestRate,
      },
    );

    return await http.get(url, headers: {
      'Content-Type': 'application/json',
    });
  }
}
