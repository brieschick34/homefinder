import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class OptimizeLoanPage extends StatefulWidget {
  // final Map<String, dynamic> loanResults;
  const OptimizeLoanPage({super.key});

  @override
  State<OptimizeLoanPage> createState() => _OptimizeLoanPageState();
}

class _OptimizeLoanPageState extends State<OptimizeLoanPage> {
  final JsonEncoder prettyEncoder = JsonEncoder.withIndent('  ');
  Map<String, dynamic>? loanResults;

  // Define all controllers
  final TextEditingController minUpfrontCostController = TextEditingController();
  final TextEditingController maxUpfrontCostController = TextEditingController();
  final TextEditingController minHouseCostController = TextEditingController();
  final TextEditingController maxHouseCostController = TextEditingController();
  final TextEditingController minMonthlyCostController = TextEditingController();
  final TextEditingController maxMonthlyCostController = TextEditingController();

  @override
  void dispose() {
    minUpfrontCostController.dispose();
    maxUpfrontCostController.dispose();
    minHouseCostController.dispose();
    maxHouseCostController.dispose();
    minMonthlyCostController.dispose();
    maxMonthlyCostController.dispose();
    super.dispose();
  }

  Widget buildInputRow(String label1, TextEditingController controller1, String label2, TextEditingController controller2) {
    return Row(
      children: [
        Expanded(
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(label1),
                TextField(controller: controller1),
              ],
            ),
          ),
        ),
        Expanded(
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(label2),
                TextField(controller: controller2),
              ],
            ),
          ),
        ),
      ],
    );
  }

  Future<void> _submitRequest() async {
    final uri = Uri.http('localhost:5000', '/api/v1/optimizeLoan', {
      'minUpFrontCost': minUpfrontCostController.text,
      'maxUpFrontCost': maxUpfrontCostController.text,
      'minimumHouseCost': minHouseCostController.text,
      'maximumHouseCost': maxHouseCostController.text,
      'minMonthlyCost': minMonthlyCostController.text,
      'maxMonthlyCost': maxMonthlyCostController.text,
    });

    try {
      final response = await http.get(uri);
      if (response.statusCode == 200) {
        print("RESPONSE: ${response.body}");
        setState(() {
          loanResults = jsonDecode(response.body);
        });
      } else {
        print("ERROR: ${response.statusCode} - ${response.body}");
      }
    } catch (e) {
      print("EXCEPTION: $e");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Optimize Loan Tool"),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            buildInputRow("Minimum Up Front Cost", minUpfrontCostController,
                "Maximum Up Front Cost", maxUpfrontCostController),
            buildInputRow("Minimum House Cost", minHouseCostController,
                "Maximum House Cost", maxHouseCostController),
            buildInputRow("Minimum Monthly Cost", minMonthlyCostController,
                "Maximum Monthly Cost", maxMonthlyCostController),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: _submitRequest,
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
                textStyle: const TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 16,
                ),
              ),
              child: const Text("Submit"),
            ),
            const SizedBox(height: 20),

            // Results section
            if (loanResults != null && loanResults!.isNotEmpty)
              ListView(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                children: loanResults!.entries.map((houseEntry) {
                  final houseCost = houseEntry.key;
                  final upFrontMap = houseEntry.value as Map;

                  return Container(
                    margin: const EdgeInsets.only(left: 0),
                    child: ExpansionTile(
                      title: Text("House Cost: \$${houseCost}"),
                      children: upFrontMap.entries.map<Widget>((upFrontEntry) {
                        final upFrontCost = upFrontEntry.key;
                        final monthlyMap = upFrontEntry.value as Map;

                        return Container(
                          margin: const EdgeInsets.only(left: 32),
                          child: ExpansionTile(
                            title: Text("  -> Up Front Cost: \$${upFrontCost}"),
                            children:
                                monthlyMap.entries.map<Widget>((monthlyEntry) {
                              final monthlyCost = monthlyEntry.key;
                              final value = monthlyEntry.value;

                              return Container(
                                margin: const EdgeInsets.only(left: 64),
                                child: ExpansionTile(
                                  title: Text(
                                      "    -> Monthly Cost: \$${monthlyCost}"),
                                  children: [
                                    Padding(
                                      padding: const EdgeInsets.all(8.0),
                                      child: Text(
                                        const JsonEncoder.withIndent('  ')
                                            .convert(value),
                                        style: const TextStyle(
                                            fontFamily: 'monospace'),
                                      ),
                                    ),
                                  ],
                                ),
                              );
                            }).toList(),
                          ),
                        );
                      }).toList(),
                    ),
                  );
                }).toList(),
              ),
          ],
        ),
      ),
    );
  }
}