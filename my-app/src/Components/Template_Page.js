import React, { useState } from "react";
import "../css/template.css";
import img1 from "../pic/img1.svg";

function Template_Page() {
  const handleSubmit = async () => {
  const topic = document.querySelector(".assess-input1 textarea").value;
  const facts = document.querySelector(".assess-input2 textarea").value;
  const strategies = document.querySelector(".assess-input3 textarea").value;
  const procedures = document.querySelector(".assess-input4 textarea").value;
  const rationales = document.querySelector(".assess-input5 textarea").value;
  
    await fetch("http://localhost:8000/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ topic, user: { facts, strategies, procedures, rationales } }),
    });
    
    console.log("Topic submitted to backend.");
  };
  

  return (
    <div className="container-fluid">
      <div className="row nav-part">
        <div className="col-4 navitem1">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="39"
            height="39"
            fill="currentColor"
            // class="bi bi-list"
            viewBox="0 0 16 16"
            className="list-ic"
          >
            <path
              fill-rule="evenodd"
              d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5"
            />
          </svg>
        </div>

        <div className="col-4 navitem2 text-center">
          <img src={img1} alt="none"></img>
        </div>

        <div className="col-4 navitem3 ">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="39"
            height="39"
            fill="currentColor"
            class="bi bi-person-fill"
            viewBox="0 0 16 16"
          >
            <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6" />
          </svg>
        </div>
      </div>

      {/* main part */}
      <div className="row main-content-part">
        {/* left */}
        <div className="col-5 left-side">
          <h3>Self Assessment Template Math</h3>
          <div className="left-side-text">
            <p>
              I want to teach you how to assess your own knowledge that you have
              about a subject area. Let’s do this by taking an example that you
              already know. Suppose you wanted to assess your own knowledge
              about solving 2-step equations of the form ax + b = c. An example
              of this type of problem is 2x + 3 = 15. If I want to be able to
              solve problems like these, I need four types of knowledge. These
              are facts, strategies, procedures and rationales. Fact are
              concepts you have that describe objects or elements. For example,
              for two step equations, I need to know what variables, constants,
              coefficients, equations, and expressions are. Strategies are
              general processes I would use to solve a problem. For two step
              equations, this would be reverse order of operations. Procedures
              are the specific steps that I would use in a strategy. So if I am
              using reverse order of operations, I need to know additive and
              multiplicative inverses. Finally, I need to know rationales which
              are the reasons why the strategies or the procedures work the way
              they do. For example, this could include things like the
              subtraction or the division property of equality that says that
              when you do the same operation to both sides of an equation, you
              preserve the value of the equation. You can think of facts as
              telling you “what”, strategies and procedures as telling you “how”
              and rationales as telling you “why”. With this in mind, this is
              how I might assess my own knowledge of solving two step equations.
            </p>
            <p>
              <strong>For facts</strong>, I need to know what variables,
              constants, coefficients, equations and expressions are. A variable
              is an unknown quantity, usually represented by a letter. A
              constant is a specific number. A coefficient is a number that you
              multiply a variable by like 2x. An equation is an expression that
              is equally to another expression and the two expressions are
              joined by an equal sign. An expression is one or more terms that
              are combined by mathematical operations like addition,
              subtraction, multiplication and division.
            </p>
            <p>
              <strong>For strategies</strong>, I need to know reverse order of
              operations which is SADMEP. This stands for subtraction, addition,
              division, multiplication, exponents and parentheses. I know that
              I’m supposed to do these in order but I don’t remember whether I’m
              supposed to do subtraction always before addition or just which
              one goes first. The same is true for division and multiplication.
            </p>
            <p>
              <strong>For procedures</strong>, I need to know additive inverse
              and multiplicative inverse. The additive inverse is taking the
              number with the opposite sign as the constant and adding it to
              both sides of the equation. The multiplicative inverse is taking
              the inverse of the coefficient of the variable and multiplying
              both sides of the equation by it. However, if the coefficient is
              negative, I’m not sure if the multiplicative inverse is supposed
              to be negative as well.
            </p>
            <p>
              <strong>For rationales</strong>, I believe the two rationales I
              need are the subtraction property of equality and the division
              property of equality. The subtraction property of equality says
              that if I subtract the same number from both sides, which is what
              I’m doing with the additive inverse, I preserve the equality.
              Similarly, the division property of equality says that if I divide
              both sides of the equation by the same number, which is what I’m
              doing with the multiplicative inverse, I preserve the equality.
            </p>
            <p>
              When I look over what I wrote, I see that I am good with my facts.
              On my strategy, I’m not sure about the order of steps in reverse
              order of operations when it comes to subtraction and addition or
              multiplication and division, so I need to learn those. On
              procedures, I’m not sure what to do with multiplicative inverses
              when the coefficient is negative, so I need to learn that as well.
              For rationales, I think I’m OK. I don’t think I have any missing
              facts/concepts that I left out that I should know or I didn’t list
              any facts/concepts where I didn’t know what they were. For the
              strategy, I believe I listed the correct strategy and parts of the
              strategy, but I wasn’t sure about some of the ordering of steps in
              the strategy. For procedures, I was good on the additive inverse
              but had a question on carrying out the multiplicative inverse when
              the coeffcient was negative. For rationales, I think I had all the
              rationales that were important and that I understood them as well.
              I don’t think I left anything out.
            </p>
          </div>
        </div>

        {/* right */}
        <div className="col right-side">
          <h3>Self Assessment</h3>

          <div className="row assess-input1">
            <span className="rs-text1">Topic</span>
            <div class="input-group">
              <textarea
                class="form-control"
                aria-label="With textarea"
              ></textarea>
            </div>
            <p className="rs-text2">Please enter the topic.</p>
          </div>

          <div className="row assess-input2">
            <p className="rs-text1">Facts</p>
            <div class="input-group">
              <textarea
                class="form-control"
                aria-label="With textarea"
              ></textarea>
            </div>
            <p className="rs-text2">Please enter the facts.</p>
          </div>

          <div className="row assess-input3">
            <p className="rs-text1">Strategies</p>
            <div class="input-group">
              <textarea
                class="form-control"
                aria-label="With textarea"
              ></textarea>
            </div>
            <p className="rs-text2">Please enter the strategies.</p>
          </div>

          <div className="row assess-input4">
            <p className="rs-text1">Procedures</p>
            <div class="input-group">
              <textarea
                class="form-control"
                aria-label="With textarea"
              ></textarea>
            </div>
            <p className="rs-text2">Please enter the procedures.</p>
          </div>
          <div className="row assess-input5">
            <p className="rs-text1">Rationales</p>
            <div class="input-group">
              <textarea
                class="form-control"
                aria-label="With textarea"
              ></textarea>
            </div>
            <p className="rs-text2">Please enter the rationales.</p>
          </div>

          <div className="button text-end">
          <button type="button" class="btn btn-primary submit" onClick={handleSubmit}>
              Submit
            </button>
          </div>
            

        </div>
      </div>
    </div>
  );
}

export default Template_Page;
