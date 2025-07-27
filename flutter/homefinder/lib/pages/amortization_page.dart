import 'package:flutter/material.dart';
import 'dart:convert';
import '../services/api_service.dart';

class AmortizationPage extends StatefulWidget {
  const AmortizationPage({super.key});

  @override
  State<AmortizationPage> createState() => _AmortizationPageState();
}

class _AmortizationPageState extends State<AmortizationPage> {
  final TextEditingController principalController = TextEditingController();
  final TextEditingController extraPaymentController = TextEditingController();
  final TextEditingController mortgageController = TextEditingController();
  final TextEditingController interestRateController = TextEditingController();
  List<List<dynamic>>? _reportData;

  @override
  void dispose() {
    principalController.dispose();
    extraPaymentController.dispose();
    mortgageController.dispose();
    interestRateController.dispose();
    super.dispose();
  }

  Future<void> _submitAmortizationRequest() async {
    final principal = principalController.text;
    final extraPayment = extraPaymentController.text;
    final mortgageAmount = mortgageController.text;
    final interestRate = interestRateController.text;

    try {
      final response = await ApiService.generateAmortizationReport(
        principal: principal,
        extraPayment: extraPayment,
        mortgageAmount: mortgageAmount,
        interestRate: interestRate,
      );

      if (response.statusCode == 200) {
        final List<dynamic> jsonData = jsonDecode(response.body);
        // Cast each inner list dynamic -> List<dynamic>
        final List<List<dynamic>> parsedData = jsonData
          .map<List<dynamic>>((row) => List<dynamic>.from(row))
          .toList();

        setState(() {
          _reportData = parsedData;
        });
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Report generated successfully!')),
        );
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Failed with status code: ${response.statusCode}')),
        );
      }
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Error: $e')),
      );
    }
  }

  Widget _buildLabeledInput(String label, TextEditingController controller) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(label,
              style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14)),
          const SizedBox(height: 5),
          TextField(
            controller: controller,
            keyboardType: TextInputType.number,
            decoration: InputDecoration(
              border: const OutlineInputBorder(),
              hintText: 'Enter $label',
              contentPadding: const EdgeInsets.symmetric(horizontal: 12),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildDataTable() {
    if (_reportData == null) {
      return const SizedBox(); // Empty container if no data yet
    }

    // Define column headers:
    final headers = [
      'Payment Number',
      'Payment Amount',
      'Interest Amount',
      'Principal',
      'Remaining Balance'
    ];

    return SingleChildScrollView(
      scrollDirection: Axis.horizontal,
      child: DataTable(
        columns: headers
            .map((header) => DataColumn(label: Text(header, style: const TextStyle(fontWeight: FontWeight.bold))))
            .toList(),
        rows: _reportData!.map((row) {
          return DataRow(
            cells: row.map((cell) {
              // Format cell to string
              final text = cell.toString();
              return DataCell(Text(text));
            }).toList(),
          );
        }).toList(),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Home Loan Amortization Report Tool"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text("Input", style: TextStyle(fontSize: 20, fontWeight: FontWeight.w600)),
            const SizedBox(height: 10),
            const Text(
              "Fill out the following fields to start using the Home Loan Amortization Report Tool!",
              style: TextStyle(fontSize: 16),
            ),
            const SizedBox(height: 20),
            _buildLabeledInput("Loan Principal", principalController),
            _buildLabeledInput("Extra Monthly Payment", extraPaymentController),
            _buildLabeledInput("Monthly Mortgage Amount", mortgageController),
            _buildLabeledInput("Interest Rate", interestRateController),
            const Spacer(),
            SizedBox(
              width: double.infinity,
              height: 64,
              child: ElevatedButton(
                onPressed: _submitAmortizationRequest,
                style: ElevatedButton.styleFrom(
                  padding: EdgeInsets.symmetric(horizontal: 32, vertical: 20),
                  textStyle: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                child: Text('Generate Report'),
              ),
            ),
            const SizedBox(height: 20),
            if (_reportData != null) Expanded(child: _buildDataTable()),
          ],
        ),
      ),
    );
  }
}
