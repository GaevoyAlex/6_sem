import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class AuthUsScreen extends StatefulWidget {
  const AuthUsScreen({super.key});

  @override
  State<AuthUsScreen> createState() => _AuthUsScreenState();
}

class _AuthUsScreenState extends State<AuthUsScreen> {
  @override
  Widget build(BuildContext context) {
    return const SingleChildScrollView(
      child: Scaffold(
        body: Column(children: [Text('User')],),
      ),
    );
  }
}
