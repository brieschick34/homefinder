import 'package:flutter/material.dart';
import 'pages/amortization_page.dart';

void main() {
  runApp(HomeLoanOptimizerApp());
}

class HomeLoanOptimizerApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Home Loan Optimizer',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  String currentPage = 'Welcome';

  final List<String> leftMenuItems = [
    'Optimize Loan',
    'Amortization Schedule',
    'Optimize Investment Property',
    'Run Tests'
  ];



  final List<String> topMenuItems = ['About Us', 'Contact Us'];

  void updatePage(String page) {
    setState(() {
      currentPage = page;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.grey[200],
        elevation: 0,
        title: InkWell(
          onTap: () => updatePage('Welcome'),
          child: Text(
            'Home Loan Optimizer',
            style: TextStyle(
              color: Colors.black,
              fontWeight: FontWeight.bold,
              fontSize: 20,
              decoration: TextDecoration.none,
            ),
          ),
        ),
        actions: topMenuItems.map((item) {
          return TextButton(
            onPressed: () => updatePage(item),
            child: Text(
              item,
              style: TextStyle(color: Colors.black),
            ),
          );
        }).toList(),
      ),
      body: Column(
        children: [
          Expanded(
            child: Row(
              children: [
                Container(
                  width: 220,
                  color: Color(0xFF9CA88D),
                  child: ListView(
                    children: leftMenuItems.map((item) {
                      final bool selected = currentPage == item;
                      return Padding(
                        padding: const EdgeInsets.symmetric(vertical: 4, horizontal: 8),
                        child: ElevatedButton.icon(
                          style: ElevatedButton.styleFrom(
                            backgroundColor: selected ? Colors.black87 : Colors.white,
                            foregroundColor: selected ? Colors.white : Colors.black87,
                            alignment: Alignment.centerLeft,
                            padding: EdgeInsets.symmetric(vertical: 16, horizontal: 12),
                          ),
                          onPressed: () => updatePage(item),
                          icon: Icon(Icons.circle, size: 20),
                          label: Text(item, style: TextStyle(fontSize: 16)),
                        ),
                      );
                    }).toList(),
                  ),
                ),

                Expanded(
                  child: Padding(
                    padding: const EdgeInsets.all(24.0),
                    child: _buildPageContent(),
                  ),
                ),
              ],
            ),
          ),
          Container(
            color: Colors.grey[200],
            padding: EdgeInsets.all(16),
            alignment: Alignment.center,
            child: Text(
              'Copyright © 2025 Rieschick Industries',
              style: TextStyle(fontSize: 14),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildPageContent() {
  switch (currentPage) {
    case 'Amortization Schedule':
      return AmortizationPage(); // This now has its own controllers and logic

    case 'Optimize Loan':
    case 'Optimize Investment Property':
    case 'Run Tests':
    case 'About Us':
    case 'Contact Us':
      return Center(
        child: Text(
          currentPage,
          style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold),
        ),
      );

    case 'Welcome':
    default:
      return Center(
        child: Text(
          'Welcome to Home Loan Optimizer!',
          style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold),
        ),
      );
  }
}


  Widget _buildLabeledTextField(String label, TextEditingController controller) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          label,
          style: TextStyle(fontWeight: FontWeight.w600, fontSize: 16),
        ),
        SizedBox(height: 8),
        TextField(
          controller: controller,
          decoration: InputDecoration(
            border: OutlineInputBorder(),
            hintText: 'Enter $label',
            contentPadding: EdgeInsets.symmetric(horizontal: 12, vertical: 10),
          ),
          keyboardType: TextInputType.numberWithOptions(decimal: true),
        ),
      ],
    );
  }

}