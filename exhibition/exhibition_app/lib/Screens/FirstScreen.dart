import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class FirstScreen extends StatefulWidget {
  FirstScreen({Key? key}) : super(key: key ?? UniqueKey());

  @override
  State<FirstScreen> createState() => _FirstScreenState();
}

class _FirstScreenState extends State<FirstScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        body:Padding(
            padding: const EdgeInsets.only(top: 120,),
            child: Column(children: [
              const GradientText(
                'Online exhibition',
                style: TextStyle(fontSize: 40,),
                gradient: LinearGradient(colors: [
                  Color.fromARGB(255, 104, 48, 246),
                  Color.fromARGB(255, 255, 0, 195),
                  Color.fromARGB(255, 211, 54, 255),
                ]),
              ),
              const SizedBox(height: 130),
              const Text('Choose the authentification mode',style: TextStyle(fontSize: 18,fontWeight: FontWeight.w200),),

              const SizedBox(height: 10,),
              GestureDetector(
                onTap: () {
                  Navigator.pushNamed(context, '/authUser');
                },
                child: Padding(
                  padding: const EdgeInsets.only(left: 100,right: 100),
                  child: Container(
                    decoration: BoxDecoration(
                        gradient: const LinearGradient(
                          colors:<Color>[
                            Color(0xffc762ba),
                            Color(0xffb563d0),
                            Color(0xff733bff),
                          ], // Gradient from https://learnui.design/tools/gradient-generator.html
                          tileMode: TileMode.decal, ),
                        borderRadius: BorderRadius.circular(20),
                        border: Border.all(width: 1)
                    ),
                    alignment: Alignment.center,
                    child: const Padding(
                      padding: EdgeInsets.only(top: 20,bottom: 20),
                      child: Text('Auth with User',style: TextStyle(fontSize: 20,color: CupertinoColors.white),),
                    ),),
                ),
              ),
              const SizedBox(height: 20,),
              GestureDetector(
                onTap: () {
                  Navigator.pushNamed(context, '/authCreators');
                },
                child: Padding(
                  padding: const EdgeInsets.only(left: 100,right: 100),
                  child: Container(
                    decoration: BoxDecoration(
                      gradient: const LinearGradient(
                          colors:<Color>[
                            Color(0xff745ce1),
                            Color(0xffbd60f3),
                            Color(0xfffa6bff),
                          ], // Gradient from https://learnui.design/tools/gradient-generator.html
                        tileMode: TileMode.decal, ),
                      borderRadius: BorderRadius.circular(20),
                      border: Border.all(width: 1)
                    ),
                    alignment: Alignment.center,
                    child: Padding(
                      padding: const EdgeInsets.only(top: 20,bottom: 20),
                      child: Text('Creators',style: TextStyle(fontSize: 20,color: CupertinoColors.white),),
                    ),),
                ),
              )
            ],),
          ),

    );
  }
}

class GradientText extends StatelessWidget {
  const GradientText(
      this.text, {super.key,
        required this.gradient,
        this.style,
      });

  final String text;
  final TextStyle? style;
  final Gradient gradient;

  @override
  Widget build(BuildContext context) {
    return ShaderMask(
      blendMode: BlendMode.srcIn,
      shaderCallback: (bounds) => gradient.createShader(
        Rect.fromLTWH(0, 0, bounds.width, bounds.height),
      ),
      child: Text(text, style: style),
    );
  }
}

