import 'package:english_words/english_words.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

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
        backgroundColor: Color(0xFF9CA88D),
        title: InkWell(
          onTap: () => updatePage('Welcome'),
          child: Text(
            'Home Loan Optimizer',
            style: TextStyle(
              color: Colors.black,
              fontWeight: FontWeight.bold,
              fontSize: 20,
              decoration: TextDecoration.none, // Optional: visual cue it's clickable
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
                  width: 220, // fixed width for menu
                  color: Color(0xFFB0C4A0), // your muted grayish green background
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
                  child: Center(
                    child: Text(
                      currentPage,
                      style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold),
                    ),
                  ),
                ),
              ],
            ),
          ),
          Container(
            color: Color(0xFF9CA88D),
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
}